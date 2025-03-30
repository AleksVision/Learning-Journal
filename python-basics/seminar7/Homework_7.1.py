import os
import shutil
import argparse
from typing import List, Optional

def batch_rename_files(directory: str, base_name: str, num_digits: int, old_extension: str, 
                      new_extension: str, name_range: tuple, in_subdirectories: bool = False) -> None:
    """
    Функция группового переименования файлов в каталоге (и подкаталогах).
    """
    def get_files(directory: str, extension: str, include_subdirectories: bool) -> List[str]:
        files = []
        for root, _, files_in_dir in os.walk(directory):
            if not include_subdirectories and root != directory:
                continue
            for file in files_in_dir:
                if file.endswith(extension):
                    files.append(os.path.join(root, file))
        return sorted(files)  # Сортируем файлы для предсказуемого порядка

    try:
        # Получаем файлы для переименования
        files_to_rename = get_files(directory, old_extension, in_subdirectories)
        
        if not files_to_rename:
            print(f"Не найдено файлов с расширением {old_extension}")
            return

        # Переименование файлов
        for index, old_file_path in enumerate(files_to_rename, start=1):
            try:
                # Получаем компоненты пути
                dir_path = os.path.dirname(old_file_path)
                filename = os.path.basename(old_file_path)
                
                # Извлекаем часть имени согласно диапазону
                name_part = filename[name_range[0]-1:name_range[1]]
                
                # Формируем новое имя
                new_filename = f"{name_part}{base_name}{str(index).zfill(num_digits)}.{new_extension}"
                new_file_path = os.path.join(dir_path, new_filename)
                
                # Используем shutil.move вместо os.rename для большей надежности
                shutil.move(old_file_path, new_file_path)
                print(f"Успешно переименован: {os.path.basename(old_file_path)} -> {os.path.basename(new_file_path)}")
                
            except Exception as e:
                print(f"Ошибка при переименовании {old_file_path}: {e}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

def create_test_files(test_dir: str) -> None:
    """Создает тестовую структуру файлов."""
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    os.makedirs(os.path.join(test_dir, 'subfolder'))
    
    test_files = [
        ('test_file001.txt', test_dir),
        ('test_file002.txt', test_dir),
        ('test_file003.txt', os.path.join(test_dir, 'subfolder'))
    ]
    
    for filename, path in test_files:
        with open(os.path.join(path, filename), 'w') as f:
            f.write('Test content')
    
    print("✅ Тестовые файлы созданы успешно")

def parse_arguments() -> argparse.Namespace:
    """Парсинг аргументов командной строки."""
    parser = argparse.ArgumentParser(description='Групповое переименование файлов')
    parser.add_argument('--dir', default='test_folder', help='Директория с файлами')
    parser.add_argument('--base', default='_new', help='Базовое имя для новых файлов')
    parser.add_argument('--digits', type=int, default=3, help='Количество цифр в номере')
    parser.add_argument('--old-ext', default='.txt', help='Старое расширение')
    parser.add_argument('--new-ext', default='pdf', help='Новое расширение')
    parser.add_argument('--range', type=int, nargs=2, default=[1, 4], help='Диапазон для части имени')
    parser.add_argument('--recursive', action='store_true', help='Рекурсивный поиск')
    parser.add_argument('--test', action='store_true', help='Создать тестовые файлы')
    
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    
    try:
        if args.test:
            create_test_files(args.dir)
        
        batch_rename_files(
            directory=args.dir,
            base_name=args.base,
            num_digits=args.digits,
            old_extension=args.old_ext,
            new_extension=args.new_ext,
            name_range=tuple(args.range),
            in_subdirectories=args.recursive
        )
        
        print("\n✨ Переименование завершено успешно!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
