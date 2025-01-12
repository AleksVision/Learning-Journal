# ========================================
# ИНТЕРАКТИВНАЯ ШПАРГАЛКА ПО PYTHON
# ========================================
# Этот файл можно как читать для справки,
# так и запускать для проверки примеров
# ========================================

def show_section(name):
    """Функция для красивого отображения заголовков разделов"""
    print(f"\n{'='*50}\n{name}\n{'='*50}")

# 1. ОСНОВНЫЕ ТИПЫ ДАННЫХ
# =======================
def demonstrate_data_types():
    show_section("1. Основные типы данных")
    
    # Числа
    целое = 42
    дробное = 3.14
    print(f"Целое число: {целое} (тип: {type(целое)})")
    print(f"Дробное число: {дробное} (тип: {type(дробное)})")

    # Строки
    строка = "Привет, мир!"
    print(f"\nСтрока: {строка}")
    print(f"Длина строки: {len(строка)}")
    print(f"Верхний регистр: {строка.upper()}")
    print(f"Нижний регистр: {строка.lower()}")

    # Списки
    список = [1, "два", 3.0, [4, 5]]
    print(f"\nСписок: {список}")
    print(f"Первый элемент: {список[0]}")
    print(f"Последний элемент: {список[-1]}")

    # Словари
    словарь = {
        "имя": "Иван",
        "возраст": 25,
        "город": "Москва"
    }
    print(f"\nСловарь: {словарь}")
    print(f"Значение по ключу 'имя': {словарь['имя']}")

# 2. РАБОТА СО СТРОКАМИ
# ====================
def demonstrate_strings():
    show_section("2. Работа со строками")
    
    текст = "  Привет, Python!  "
    print(f"Исходный текст: '{текст}'")
    print(f"Убрать пробелы: '{текст.strip()}'")
    print(f"Замена: '{текст.replace('Python', 'Мир')}'")
    print(f"Разделить по пробелам: {текст.split()}")
    
    # f-строки
    имя = "Анна"
    возраст = 25
    print(f"\nf-строка: Привет, {имя}! Тебе {возраст} лет")

# 3. РАБОТА СО СПИСКАМИ
# ====================
def demonstrate_lists():
    show_section("3. Работа со списками")
    
    список = [1, 2, 3, 4, 5]
    print(f"Исходный список: {список}")
    
    # Добавление элементов
    список.append(6)
    print(f"После append(6): {список}")
    
    список.insert(0, 0)
    print(f"После insert(0, 0): {список}")
    
    # Удаление элементов
    удаленный = список.pop()
    print(f"Удалён элемент: {удаленный}")
    print(f"После pop(): {список}")
    
    список.remove(3)
    print(f"После remove(3): {список}")
    
    # Сортировка
    список.sort()
    print(f"После сортировки: {список}")
    список.reverse()
    print(f"После reverse(): {список}")

# 4. ЦИКЛЫ
# ========
def demonstrate_loops():
    show_section("4. Циклы")
    
    # Цикл for с range
    print("Цикл for с range(5):")
    for i in range(5):
        print(i, end=' ')
    print()
    
    # Цикл for по списку
    print("\nЦикл по списку:")
    животные = ["кот", "собака", "хомяк"]
    for животное in животные:
        print(f"У меня есть {животное}")
    
    # Цикл while
    print("\nЦикл while:")
    счетчик = 0
    while счетчик < 3:
        print(f"счетчик = {счетчик}")
        счетчик += 1

# 5. УСЛОВНЫЕ КОНСТРУКЦИИ
# ======================
def demonstrate_conditionals():
    show_section("5. Условные конструкции")
    
    def проверить_возраст(возраст):
        if возраст < 18:
            return "Доступ запрещен"
        elif возраст == 18:
            return "Вам ровно 18"
        else:
            return "Доступ разрешен"
    
    # Примеры использования
    возрасты = [16, 18, 25]
    for возраст in возрасты:
        результат = проверить_возраст(возраст)
        print(f"Возраст {возраст}: {результат}")
    
    # Сложные условия
    print("\nСложные условия:")
    оценка = 85
    посещаемость = 90
    if оценка >= 80 and посещаемость >= 80:
        print("Отличный результат!")

# 6. ФУНКЦИИ
# ==========
def demonstrate_functions():
    show_section("6. Функции")
    
    # Простая функция
    def приветствие(имя):
        return f"Привет, {имя}!"
    
    # Функция с параметром по умолчанию
    def степень(число, степень=2):
        return число ** степень
    
    # Функция с произвольным числом аргументов
    def сумма(*args):
        return sum(args)
    
    # Примеры использования
    print(приветствие("Иван"))
    print(f"2 в степени 3 = {степень(2, 3)}")
    print(f"Сумма чисел 1,2,3,4,5 = {сумма(1,2,3,4,5)}")

# 7. ОБРАБОТКА ИСКЛЮЧЕНИЙ
# =====================
def demonstrate_exceptions():
    show_section("7. Обработка исключений")
    
    def безопасное_деление(a, b):
        try:
            результат = a / b
            return f"Результат деления: {результат}"
        except ZeroDivisionError:
            return "Ошибка: деление на ноль!"
        except TypeError:
            return "Ошибка: неверный тип данных!"
    
    # Примеры использования
    print(безопасное_деление(10, 2))
    print(безопасное_деление(10, 0))
    print(безопасное_деление(10, "2"))

# ЗАПУСК ВСЕХ ДЕМОНСТРАЦИЙ
# =======================
if __name__ == "__main__":
    print("ИНТЕРАКТИВНАЯ ШПАРГАЛКА ПО PYTHON")
    print("Запуск всех демонстраций...\n")
    
    demonstrate_data_types()
    demonstrate_strings()
    demonstrate_lists()
    demonstrate_loops()
    demonstrate_conditionals()
    demonstrate_functions()
    demonstrate_exceptions()
    
    print("\nВсе демонстрации завершены!")