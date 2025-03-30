'''
Задание 8.7
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
'''
import os
from typing import List, Dict, Any
from file_utils.file_formats import save_to_json, save_to_csv, save_to_pickle

def get_directory_size(path: str) -> int:
    """Вычисляет общий размер файлов в директории."""
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                total_size += os.path.getsize(filepath)
            except OSError as e:
                print(f"Ошибка при получении размера {filepath}: {e}")
    return total_size

def process_directory(directory: str, 
                     json_filename: str = 'files_info.json',
                     csv_filename: str = 'files_info.csv',
                     pickle_filename: str = 'files_info.pkl') -> bool:
    """Обрабатывает директорию и сохраняет информацию в разных форматах."""
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Директория {directory} не найдена")
            
        file_info = []
        for dirpath, dirnames, filenames in os.walk(directory):
            # Обработка файлов
            for name in filenames:
                path = os.path.join(dirpath, name)
                file_info.append({
                    'name': name,
                    'path': path,
                    'parent': os.path.basename(dirpath),
                    'type': 'file',
                    'size': os.path.getsize(path)
                })
            
            # Обработка директорий
            for name in dirnames:
                path = os.path.join(dirpath, name)
                file_info.append({
                    'name': name,
                    'path': path,
                    'parent': os.path.basename(dirpath),
                    'type': 'directory',
                    'size': get_directory_size(path)
                })
        
        # Сохранение в разных форматах
        save_to_json(file_info, json_filename)
        save_to_csv(file_info, csv_filename)
        save_to_pickle(file_info, pickle_filename)
        
        print(f"✅ Данные сохранены в файлы:")
        print(f"📄 JSON: {json_filename}")
        print(f"📊 CSV: {csv_filename}")
        print(f"🗃️ Pickle: {pickle_filename}")
        
        return True
        
    except Exception as e:
        print(f"❌ Ошибка при обработке директории: {e}")
        return False
