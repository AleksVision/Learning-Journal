'''
Задание 8.3
Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''

import json
import csv
import os
from typing import Dict, Any

def json_to_csv(json_filename: str = 'user_data.json', 
                csv_filename: str = 'res.csv') -> None:
    """
    Конвертирует JSON файл в CSV формат.
    
    Args:
        json_filename (str): Имя входного JSON файла
        csv_filename (str): Имя выходного CSV файла
    """
    try:
        # Получаем пути к файлам
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, json_filename)
        csv_path = os.path.join(current_dir, csv_filename)
        
        # Проверяем существование JSON файла
        if not os.path.exists(json_path):
            raise FileNotFoundError(f"Файл {json_filename} не найден")
            
        # Загружаем JSON данные
        with open(json_path, 'r', encoding='utf-8') as f_json:
            db = json.load(f_json)
        
        # Записываем в CSV
        with open(csv_path, 'w', newline='', encoding='utf-8') as f_csv:
            writer = csv.writer(f_csv)
            writer.writerow(['ID', 'Код', 'Имя'])  # Заголовки на русском
            
            for key, value in db.items():
                for sub_key, name in value.items():
                    writer.writerow([key, sub_key, name])
                    
        print(f"Данные успешно сконвертированы в {csv_path}")
            
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")

if __name__ == "__main__":
    json_to_csv()
