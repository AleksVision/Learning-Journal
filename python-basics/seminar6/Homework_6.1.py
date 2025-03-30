'''
Задание 6.1
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
Проверка даты должна быть в формате YYYY-MM-DD.
Пример:
python date_checker.py 2023-10-01
# Вывод:
# Дата 2023-10-01 корректна.
# Примечание: Если дата некорректна, необходимо вывести сообщение об ошибке.
'''
import sys
from datetime import datetime
from typing import Optional
def is_valid_date(date_string: str) -> Optional[datetime]:
    """
    Проверяет, является ли строка корректной датой в формате YYYY-MM-DD.
    
    :param date_string: Дата в формате YYYY-MM-DD.
    :return: datetime объект, если дата корректна, иначе None.
    """
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
    except ValueError:
        return None
def main():
    if len(sys.argv) != 2:
        print("Использование: python date_checker.py YYYY-MM-DD")
        sys.exit(1)
    date_string = sys.argv[1]
    valid_date = is_valid_date(date_string)
    if valid_date:
        print(f"Дата {date_string} корректна.")
    else:
        print(f"Дата {date_string} некорректна.")
if __name__ == "__main__":
    main()
