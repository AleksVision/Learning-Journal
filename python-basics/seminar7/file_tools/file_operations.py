# file_tools/file_operations.py
import os
from typing import List

def get_files(directory: str, extension: str, include_subdirectories: bool) -> List[str]:
    """
    Получает список файлов с указанным расширением из каталога и подкаталогов.
    
    :param directory: Путь к каталогу.
    :param extension: Расширение файлов, которые нужно получить.
    :param include_subdirectories: Флаг, указывающий, нужно ли учитывать файлы в подкаталогах.
    :return: Список файлов с нужным расширением.
    """
    files = []
    for root, dirs, files_in_dir in os.walk(directory):
        if not include_subdirectories and root != directory:
            continue
        for file in files_in_dir:
            if file.endswith(extension):
                files.append(os.path.join(root, file))
    return files
