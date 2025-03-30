"""
Пакет для работы с файлами разных форматов.
Поддерживает сканирование директорий и сохранение в JSON, CSV и Pickle форматах.
"""

from .file_formats import save_to_json, save_to_csv, save_to_pickle
from .file_scanner import process_directory, get_directory_size

__all__ = [
    'save_to_json',
    'save_to_csv', 
    'save_to_pickle',
    'process_directory',
    'get_directory_size'
]

__version__ = '0.1.0'
