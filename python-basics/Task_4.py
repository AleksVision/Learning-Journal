from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Задаем URL
url = "https://www.avito.ru/moskva_i_mo/remont_i_stroitelstvo/stroymaterialy/beton-ASgBAgICA0RYoAKmvg2YxDXYoRTe6I4D"

# Настройки прокси (если необходимо)
proxy = None  # Замените на ваш прокси, если есть

# Настройки Selenium
options = webdriver.ChromeOptions()
if proxy:
    options.add_argument(f'--proxy-server={proxy}')
options.add_argument('--headless')  # Запускаем в фоновом режиме
options.add_argument('--disable-gpu')

# Запускаем браузер
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get(url)
    time.sleep(5)  # Ждем, чтобы страница загрузилась полностью

    # Парсим ссылки на объявления
    items = driver.find_elements(By.XPATH, '//div[@data-marker="item"]')
    print(f"Найдено объявлений: {len(items)}")

    links = []
    for item in items:
        try:
            title = item.find_element(By.XPATH, './/h3').text if item.find_elements(By.XPATH, './/h3') else "Название не найдено"
            price = item.find_element(By.XPATH, './/meta[@itemprop="price"]').get_attribute('content') if item.find_elements(By.XPATH, './/meta[@itemprop="price"]') else "Цена не найдена"
            
            # Сохраняем ссылку на объявление
            link = item.find_element(By.XPATH, './/a').get_attribute('href')
            links.append((title, price, link))
        except Exception as e:
            print(f"Ошибка: {e}")
        
    for title, price, link in links:
        try:
            driver.get(link)
            time.sleep(5)  # Ждем, чтобы страница загрузилась полностью
            
            # Извлекаем информацию о продавце и контактах
            seller = driver.find_element(By.XPATH, '//div[@data-marker="seller-info/name"]').text if driver.find_elements(By.XPATH, '//div[@data-marker="seller-info/name"]') else "Продавец не найден"
            contacts = driver.find_element(By.XPATH, '//div[contains(@class, "seller-phones")]/a').get_attribute('href') if driver.find_elements(By.XPATH, '//div[contains(@class, "seller-phones")]/a') else "Контакты не найдены"
            
            print(f"Продукт: {title}\nЦена: {price}\nПродавец: {seller}\nКонтакты: {contacts}\n")
            
            # Возвращаемся к списку объявлений
            driver.back()
            time.sleep(5)  # Ждем, чтобы страница загрузилась полностью
        except Exception as e:
            print(f"Ошибка: {e}")

finally:
    driver.quit()
