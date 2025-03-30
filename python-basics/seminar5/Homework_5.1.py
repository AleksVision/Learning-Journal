'''
Задача 5.1
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''
import os
def split_path(file_path):
    """
    Разделяет абсолютный путь на директорию, имя файла и расширение файла.

    :param file_path: Абсолютный путь до файла.
    :return: Кортеж (директория, имя файла, расширение файла).
    """
    # Получаем директорию
    directory = os.path.dirname(file_path)
    
    # Получаем имя файла с расширением
    file_name_with_extension = os.path.basename(file_path)
    
    # Разделяем имя файла и расширение
    file_name, file_extension = os.path.splitext(file_name_with_extension)
    
    return directory, file_name, file_extension
# Пример использования функции
file_path = "/home/user/documents/file.txt"
directory, file_name, file_extension = split_path(file_path)
print("Directory:", directory)
print("File Name:", file_name)
print("File Extension:", file_extension)
'''
# Вывод:
Directory: /home/user/documents
File Name: file
File Extension: .txt
'''
