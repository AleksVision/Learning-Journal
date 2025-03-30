# File Tools Package

Пакет для работы с файлами и дополнительными утилитами.

## Установка

```bash
pip install -e .
```

## Использование

```python
from file_tools import (
    get_files,           # Поиск файлов
    batch_rename_files,  # Групповое переименование
    is_safe,            # Проверка расстановки ферзей
    fibonacci           # Генератор Фибоначчи
)
```

### Примеры

1. Поиск файлов:

```python
files = get_files("my_directory", ".txt", True)
```

2. Переименование файлов:

```python
batch_rename_files(
    directory="my_directory",
    base_name="new_file",
    num_digits=3,
    old_extension=".txt",
    new_extension="pdf",
    name_range=(1, 4)
)
```

3. Проверка расстановки ферзей:

```python
queens = [(1, 1), (2, 5), (3, 8), (4, 6),
         (5, 3), (6, 7), (7, 2), (8, 4)]
is_valid = is_safe(queens)
```

4. Генерация чисел Фибоначчи:

```python
for number in fibonacci(100):
    print(number)
```
