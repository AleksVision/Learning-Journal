import os
from typing import List, Dict, Any

def get_directory_size(path: str) -> int:
    """Получает размер директории в байтах."""
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_directory_size(entry.path)
    return total

def process_directory(path: str) -> List[Dict[str, Any]]:
    """Сканирует директорию и собирает информацию о файлах."""
    result = []
    abs_path = os.path.abspath(path)
    
    for root, dirs, files in os.walk(abs_path):
        parent = os.path.basename(root)
        
        # Обработка файлов
        for name in files:
            file_path = os.path.join(root, name)
            result.append({
                'name': name,
                'type': 'file',
                'parent': parent,
                'size': os.path.getsize(file_path),
                'path': file_path
            })
        
        # Обработка директорий
        for name in dirs:
            dir_path = os.path.join(root, name)
            result.append({
                'name': name,
                'type': 'directory',
                'parent': parent,
                'size': get_directory_size(dir_path),
                'path': dir_path
            })
    
    return result
