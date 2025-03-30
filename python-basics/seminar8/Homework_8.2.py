'''Задание 8.2
Напишите функцию, которая в бесконечном цикле запрашивает имя,
личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.'''
import json
import os
import random
import string
from datetime import datetime
from typing import Dict, List
# Определяем путь к файлу JSON
JSON_FILE = 'user_data.json'
# Функция для генерации уникального идентификатора
def generate_unique_id(length: int = 8) -> str:
    """Генерирует уникальный идентификатор."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
# Функция для загрузки данных из JSON файла
def load_data() -> Dict[int, Dict[str, str]]:
    """Загружает данные из JSON файла."""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}
# Функция для сохранения данных в JSON файл
def save_data(data: Dict[int, Dict[str, str]]) -> None:
    """Сохраняет данные в JSON файл."""
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
# Функция для добавления пользователя
def add_user(data: Dict[int, Dict[str, str]], name: str, user_id: str, access_level: int) -> None:
    """Добавляет пользователя в данные."""
    if access_level not in data:
        data[access_level] = {}
    data[access_level][user_id] = name
# Функция для проверки уникальности идентификатора
def is_unique_id(data: Dict[int, Dict[str, str]], user_id: str) -> bool:
    """Проверяет уникальность идентификатора."""
    for level in data.values():
        if user_id in level:
            return False
    return True
# Основная функция для запуска программы
def main() -> None:
    """Основная функция для запуска программы."""
    data = load_data()
    while True:
        name = input("Введите имя пользователя: ").strip()
        if not name:
            print("Имя не может быть пустым. Попробуйте снова.")
            continue
        try:
            access_level = int(input("Введите уровень доступа (от 1 до 7): "))
            if access_level < 1 or access_level > 7:
                raise ValueError
        except ValueError:
            print("Некорректный уровень доступа. Попробуйте снова.")
            continue
        user_id = generate_unique_id()
        while not is_unique_id(data, user_id):
            user_id = generate_unique_id()
        add_user(data, name, user_id, access_level)
        save_data(data)
        print(f"Пользователь {name} с ID {user_id} и уровнем доступа {access_level} добавлен.")
        print(f"Текущие данные: {json.dumps(data, indent=4, ensure_ascii=False)}")
        cont = input("Хотите добавить еще одного пользователя? (да/нет): ").strip().lower()
        if cont != 'да':
            break
if __name__ == "__main__":
    main()
