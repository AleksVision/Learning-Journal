'''
Задание 8.6
Напишите функцию, которая преобразует ріс файл хранящий список словарей в табличный csv файл.
Для тестированию возьмите pickle версию файла из задачи 4 семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
'''
import pickle
import csv
import os
from typing import List, Dict, Any

def pickle_to_csv(pickle_filename: str, csv_filename: str) -> bool:
    """
    Преобразует Pickle файл, содержащий список словарей, в CSV файл.
    
    Args:
        pickle_filename (str): Путь к Pickle файлу
        csv_filename (str): Путь к CSV файлу
    
    Returns:
        bool: True если конвертация успешна, иначе False
    """
    try:
        # Получаем абсолютные пути к файлам
        current_dir = os.path.dirname(os.path.abspath(__file__))
        pickle_path = os.path.join(current_dir, pickle_filename)
        csv_path = os.path.join(current_dir, csv_filename)
        
        # Проверяем существование файла
        if not os.path.exists(pickle_path):
            raise FileNotFoundError(f"Файл {pickle_filename} не найден")
        
        # Открываем Pickle файл для чтения
        with open(pickle_path, 'rb') as f_pickle:
            data = pickle.load(f_pickle)
        
        # Проверяем, что данные — это список словарей
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("Файл должен содержать список словарей")
        
        if not data:
            raise ValueError("Файл не содержит данных")
        
        # Извлекаем ключи словаря для заголовков столбцов
        headers = list(data[0].keys())
        
        # Открываем CSV файл для записи
        with open(csv_path, 'w', newline='', encoding='utf-8') as f_csv:
            writer = csv.DictWriter(f_csv, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        
        print(f"✅ Данные успешно записаны в {csv_filename}")
        return True
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

if __name__ == "__main__":
    # Тестируем на файле из предыдущего задания
    result = pickle_to_csv('output.pkl', 'converted_data.csv')
    
    if result:
        print("\nПроверьте содержимое файла converted_data.csv")
