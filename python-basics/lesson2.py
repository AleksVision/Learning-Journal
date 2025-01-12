import os
import shutil
import json
import csv
import hashlib
import tempfile
from pathlib import Path
from typing import Generator, Dict, List, Any

# =============================================
# Урок 2: Улучшенное руководство по работе с файлами
# =============================================


"""
СОДЕРЖАНИЕ УРОКА:
1. Основные режимы работы с файлами
2. Безопасные операции с файлами
3. Эффективная работа с большими файлами
4. Продвинутая работа с путями
5. Работа с различными форматами
6. Управление временными файлами
7. Операции с директориями
8. Поиск и обработка дубликатов
9. Практические примеры
10. Продвинутые техники

Каждый раздел содержит:
- Подробное описание функциональности
- Примеры использования
- Обработку возможных ошибок
- Рекомендации по оптимальному использованию
"""

class FileOperationError(Exception):
    """Пользовательский класс исключений для операций с файлами"""
    pass

# 1. ОСНОВНЫЕ РЕЖИМЫ РАБОТЫ С ФАЙЛАМИ
# =================================
def demonstrate_file_modes() -> None:
    """
    Демонстрирует различные режимы работы с файлами и безопасную обработку ошибок.
    
    Режимы:
    - 'r': чтение (по умолчанию)
    - 'w': запись (создаёт новый или перезаписывает)
    - 'a': добавление в конец
    - 'x': эксклюзивное создание
    - 'r+': чтение и запись
    - 'w+': запись и чтение (перезаписывает)
    - 'a+': добавление и чтение
    
    Дополнительные флаги:
    - 'b': бинарный режим
    - 't': текстовый режим (по умолчанию)
    """
    print("\n=== Демонстрация режимов работы с файлами ===")
    
    # Безопасное создание файла
    try:
        with open('new_file.txt', 'x', encoding='utf-8') as f:
            f.write('Новый файл создан\n')
    except FileExistsError:
        print("Файл уже существует!")
    except PermissionError:
        print("Нет прав на создание файла")
    except OSError as e:
        print(f"Системная ошибка: {e}")

    # Демонстрация различных режимов
    try:
        # Режим w+ позволяет читать и писать
        with open('test.txt', 'w+', encoding='utf-8') as f:
            f.write('Тест режима w+\n')
            f.flush()  # Принудительная запись буфера
            f.seek(0)  # Возврат к началу файла
            content = f.read()
            print(f"Прочитано в режиме w+: {content}")
    except OSError as e:
        print(f"Ошибка при работе с файлом: {e}")

# 2. БЕЗОПАСНЫЕ ОПЕРАЦИИ С ФАЙЛАМИ
# ==============================
class SafeFileHandler:
    """
    Класс для безопасной работы с файлами.
    Предоставляет методы для выполнения основных файловых операций
    с надёжной обработкой ошибок.
    """
    
    @staticmethod
    def safe_read(filename: str) -> str:
        """Безопасное чтение файла с обработкой всех возможных ошибок."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            raise FileOperationError(f"Файл {filename} не найден")
        except PermissionError:
            raise FileOperationError(f"Нет прав на чтение файла {filename}")
        except UnicodeDecodeError:
            raise FileOperationError(f"Ошибка декодирования файла {filename}")
        except Exception as e:
            raise FileOperationError(f"Непредвиденная ошибка: {e}")

    @staticmethod
    def safe_write(filename: str, content: str) -> None:
        """Безопасная запись в файл с обработкой всех возможных ошибок."""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
        except PermissionError:
            raise FileOperationError(f"Нет прав на запись в файл {filename}")
        except OSError as e:
            raise FileOperationError(f"Ошибка записи в файл {filename}: {e}")

# 3. ЭФФЕКТИВНАЯ РАБОТА С БОЛЬШИМИ ФАЙЛАМИ
# =====================================
def process_large_file(filename: str, chunk_size: int = 8192) -> Generator[str, None, None]:
    """
    Эффективно обрабатывает большой файл, читая его по частям.
    
    Args:
        filename: путь к файлу
        chunk_size: размер читаемого блока в байтах
    
    Yields:
        Строки из файла
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Читаем файл построчно, что эффективно для больших файлов
            for line in file:
                yield line.strip()
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")

def demonstrate_large_file_processing():
    """Демонстрирует эффективную обработку больших файлов."""
    print("\n=== Демонстрация обработки больших файлов ===")
    
    # Создаём тестовый большой файл
    try:
        with open('large_file.txt', 'w', encoding='utf-8') as f:
            for i in range(1000):
                f.write(f"Строка {i}\n")
        
        # Эффективное чтение
        for line in process_large_file('large_file.txt'):
            pass  # Обработка каждой строки
    except Exception as e:
        print(f"Ошибка при демонстрации: {e}")
    finally:
        # Очистка после демонстрации
        if os.path.exists('large_file.txt'):
            os.remove('large_file.txt')

# 4. ПРОДВИНУТАЯ РАБОТА С ПУТЯМИ
# ===========================
def demonstrate_path_operations():
    """
    Демонстрирует современные методы работы с путями используя pathlib.
    Pathlib предоставляет более удобный и объектно-ориентированный интерфейс
    по сравнению с os.path.
    """
    print("\n=== Демонстрация работы с путями ===")
    
    try:
        # Создаём путь к текущей директории
        current_path = Path.cwd()
        print(f"Текущая директория: {current_path}")
        
        # Создаём новую директорию и файл
        test_dir = current_path / 'test_dir'
        test_dir.mkdir(exist_ok=True)
        
        test_file = test_dir / 'test.txt'
        test_file.write_text('Тест pathlib', encoding='utf-8')
        
        # Демонстрация различных операций с путями
        print(f"Родительская директория: {test_file.parent}")
        print(f"Имя файла: {test_file.name}")
        print(f"Расширение: {test_file.suffix}")
        print(f"Существует: {test_file.exists()}")
        
    except Exception as e:
        print(f"Ошибка при работе с путями: {e}")

# 5. РАБОТА С РАЗЛИЧНЫМИ ФОРМАТАМИ
# ============================
class FileFormatHandler:
    """Класс для работы с различными форматами файлов."""
    
    @staticmethod
    def process_json(filename: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Работа с JSON файлами."""
        try:
            if data:  # Запись
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                return data
            else:  # Чтение
                with open(filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except json.JSONDecodeError:
            raise FileOperationError("Ошибка декодирования JSON")
        except Exception as e:
            raise FileOperationError(f"Ошибка при работе с JSON: {e}")

    @staticmethod
    def process_csv(filename: str, data: List[List[str]] = None) -> List[List[str]]:
        """Работа с CSV файлами."""
        try:
            if data:  # Запись
                with open(filename, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerows(data)
                return data
            else:  # Чтение
                with open(filename, 'r', encoding='utf-8') as f:
                    return list(csv.reader(f))
        except Exception as e:
            raise FileOperationError(f"Ошибка при работе с CSV: {e}")

    @staticmethod
    def process_binary(filename: str, data: bytes = None) -> bytes:
        """Работа с бинарными файлами."""
        try:
            if data:  # Запись
                with open(filename, 'wb') as f:
                    f.write(data)
                return data
            else:  # Чтение
                with open(filename, 'rb') as f:
                    return f.read()
        except Exception as e:
            raise FileOperationError(f"Ошибка при работе с бинарным файлом: {e}")

# 6. УПРАВЛЕНИЕ ВРЕМЕННЫМИ ФАЙЛАМИ
# ============================
def demonstrate_temp_files():
    """
    Демонстрирует работу с временными файлами и директориями.
    Использует контекстные менеджеры для автоматической очистки.
    """
    print("\n=== Демонстрация работы с временными файлами ===")
    
    try:
        # Временный файл с автоудалением
        with tempfile.NamedTemporaryFile(mode='w+', delete=True) as temp:
            temp.write('Временные данные\n')
            temp.flush()
            temp.seek(0)
            content = temp.read()
            print(f"Прочитано из временного файла: {content}")
        
        # Временная директория
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir) / 'test.txt'
            temp_path.write_text('Тест временной директории')
            print(f"Создан файл во временной директории: {temp_path}")
            
    except Exception as e:
        print(f"Ошибка при работе с временными файлами: {e}")

# 7. ОПЕРАЦИИ С ДИРЕКТОРИЯМИ
# =======================
class DirectoryHandler:
    """Класс для работы с директориями."""
    
    @staticmethod
    def scan_directory(path: str) -> Generator[Path, None, None]:
        """Сканирует директорию и возвращает все найденные файлы."""
        try:
            for item in Path(path).rglob('*'):
                if item.is_file():
                    yield item
        except Exception as e:
            raise FileOperationError(f"Ошибка при сканировании директории: {e}")

    @staticmethod
    def create_directory_structure(base_path: str, structure: Dict) -> None:
        """Создаёт структуру директорий и файлов."""
        try:
            base = Path(base_path)
            for name, content in structure.items():
                path = base / name
                if isinstance(content, dict):
                    path.mkdir(exist_ok=True)
                    DirectoryHandler.create_directory_structure(str(path), content)
                else:
                    path.write_text(str(content))
        except Exception as e:
            raise FileOperationError(f"Ошибка при создании структуры: {e}")

# 8. ПОИСК И ОБРАБОТКА ДУБЛИКАТОВ
# ============================
class DuplicateFinder:
    """Класс для поиска дубликатов файлов."""
    
    @staticmethod
    def calculate_file_hash(filepath: Path, block_size: int = 65536) -> str:
        """
        Вычисляет SHA-256 хеш файла, читая его блоками для эффективности.
        """
        hasher = hashlib.sha256()
        try:
            with open(filepath, 'rb') as file:
                while True:
                    data = file.read(block_size)
                    if not data:
                        break
                    hasher.update(data)
            return hasher.hexdigest()
        except Exception as e:
            raise FileOperationError(f"Ошибка при вычислении хеша: {e}")

    @staticmethod
    def find_duplicates(directory: str) -> Dict[str, List[Path]]:
        """
        Находит дубликаты файлов в указанной директории.
        Возвращает словарь, где ключ - хеш файла, значение - список путей к дубликатам.
        """
        hash_dict: Dict[str, List[Path]] = {}
        try:
            for filepath in Path(directory).rglob('*'):
                if filepath.is_file():
                    file_hash = DuplicateFinder.calculate_file_hash(filepath)
                    hash_dict.setdefault(file_hash, []).append(filepath)
            
            # Оставляем только дубликаты (больше одного файла с одинаковым хешем)
            return {k: v for k, v in hash_dict.items() if len(v) > 1}
        except Exception as e:
            raise FileOperationError(f"Ошибка при поиске дубликатов: {e}")

# 9. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# =====================
def demonstrate_practical_examples():
    print("\n=== Практические примеры ===")
    
    # Подсчёт строк в файлах Python
    def count_lines_in_py_files(directory: str) -> int:
        total_lines = 0
        try:
            for filepath in Path(directory).rglob('*.py'):
                with open(filepath, 'r', encoding='utf-8') as file:
                    total_lines += sum(1 for _ in file)
        except Exception as e:
            print(f"Ошибка при подсчёте строк: {e}")
        return total_lines
    
    # Поиск дубликатов файлов
    def find_duplicates(directory: str) -> None:
        duplicates = DuplicateFinder.find_duplicates(directory)
        for file_hash, paths in duplicates.items():
            print(f"Дубликаты с хешем {file_hash}:")
            for path in paths:
                print(f"  {path}")

# 10. ПРОДВИНУТЫЕ ТЕХНИКИ
# =====================
def demonstrate_advanced_techniques():
    print("\n=== Продвинутые техники ===")
    
    # Использование контекстного менеджера
    class FileManager:
        def __init__(self, filename: str, mode: str = 'r'):
            self.filename = filename
            self.mode = mode
            self.file = None
        
        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
    
    # Использование
    with FileManager('test.txt', 'w') as file:
        file.write('Тест менеджера контекста\n')
    
    # Буферизированная запись
    with open('buffer.txt', 'w', buffering=8192) as file:
        for i in range(1000000):
            file.write(f"{i}\n")

# ЗАПУСК ВСЕХ ДЕМОНСТРАЦИЙ
# =======================
if __name__ == "__main__":
    print("УРОК 2: ПОЛНОЕ РУКОВОДСТВО ПО РАБОТЕ С ФАЙЛАМИ В PYTHON")
    print("Запуск всех демонстраций...\n")
    
    # Выполнение всех демонстраций
    demonstrate_file_modes()
    demonstrate_large_file_processing()
    demonstrate_path_operations()
    demonstrate_temp_files()
    demonstrate_practical_examples()
    demonstrate_advanced_techniques()
    
    print("\nВсе демонстрации завершены!")