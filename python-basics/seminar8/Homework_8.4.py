'''
Задание 8.4
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и идентификатора.
Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json
Имя исходного и конечного файлов передавайте как аргументы функции.'''
import csv
import json
import hashlib
import os
from typing import List, Dict, Any

def process_csv_to_json(csv_filename: str = 'res.csv', 
                       json_filename: str = 'output.json') -> bool:
    """
    Обрабатывает CSV файл и сохраняет данные в JSON.
    
    Args:
        csv_filename (str): Путь к входному CSV файлу
        json_filename (str): Путь к выходному JSON файлу
    
    Returns:
        bool: True если обработка успешна, иначе False
    """
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, csv_filename)
        json_path = os.path.join(current_dir, json_filename)
        
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV файл {csv_filename} не найден")
        
        data: List[Dict[str, Any]] = []
        
        with open(csv_path, 'r', encoding='utf-8') as f:
            # Читаем заголовки
            headers = next(csv.reader(f))
            
            # Читаем данные
            for row in csv.reader(f):
                user_id = row[0].zfill(10)  # ID до 10 цифр
                code = row[1]
                name = row[2].capitalize()  # Имя с большой буквы
                
                # Создаем хеш
                hash_input = f"{user_id}{name}"
                user_hash = hashlib.md5(hash_input.encode('utf-8')).hexdigest()
                
                # Добавляем запись
                data.append({
                    'id': user_id,
                    'code': code,
                    'name': name,
                    'hash': user_hash
                })
        
        # Сохраняем в JSON
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            
        print(f"✅ Данные успешно сохранены в {json_filename}")
        return True
            
    except Exception as e:
        print(f"❌ Ошибка обработки: {e}")
        return False

if __name__ == "__main__":
    process_csv_to_json()
