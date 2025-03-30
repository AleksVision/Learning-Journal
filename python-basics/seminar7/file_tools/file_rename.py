# file_tools/file_rename.py
import os
from typing import Tuple

def batch_rename_files(directory: str, base_name: str, num_digits: int, old_extension: str, new_extension: str, 
                        name_range: Tuple[int, int], in_subdirectories: bool = False):
    """
    Функция группового переименования файлов в каталоге (и подкаталогах).
    
    :param directory: Путь к каталогу.
    :param base_name: Базовое имя для новых файлов (к нему будет добавлен порядковый номер).
    :param num_digits: Количество цифр в порядковом номере.
    :param old_extension: Расширение файлов, которые нужно переименовать.
    :param new_extension: Расширение для новых файлов.
    :param name_range: Диапазон символов из исходного имени (например, [3, 6]).
    :param in_subdirectories: Параметр, указывающий, нужно ли переименовывать файлы в подкаталогах.
    """
    from .file_operations import get_files  # Импорт функции для получения файлов
    
    files_to_rename = get_files(directory, old_extension, in_subdirectories)

    # Переименование файлов
    for index, old_file_path in enumerate(files_to_rename, start=1):
        # Получаем имя файла без пути
        filename = os.path.basename(old_file_path)
        
        # Извлекаем часть имени согласно диапазону
        start, end = name_range
        new_name_part = filename[start-1:end]

        # Формируем новое имя
        new_filename = f"{new_name_part}{base_name}{str(index).zfill(num_digits)}.{new_extension}"
        
        # Полный путь для нового имени файла
        new_file_path = os.path.join(os.path.dirname(old_file_path), new_filename)
        
        # Переименовываем файл
        os.rename(old_file_path, new_file_path)
        print(f"Переименован: {old_file_path} -> {new_file_path}")
