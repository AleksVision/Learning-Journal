'''
Задание 6.3
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''
import random
from typing import List, Tuple

# Функция для проверки, не бьют ли ферзи друг друга
def is_safe(queens: List[Tuple[int, int]]) -> bool:
    """
    Проверяет, не бьют ли друг друга ферзи, расставленные на доске.
    
    :param queens: Список из 8 пар чисел, где каждая пара — это координаты ферзя (строка, столбец).
    :return: True, если ферзи не бьют друг друга, иначе False.
    """
    rows = set()  # Множество для проверки уникальности строк
    cols = set()  # Множество для проверки уникальности столбцов
    diag1 = set()  # Множество для проверки уникальности первой диагонали (x - y)
    diag2 = set()  # Множество для проверки уникальности второй диагонали (x + y)

    for row, col in queens:
        # Проверка, не совпадает ли строка, столбец или диагональ с предыдущими
        if row in rows or col in cols or (row - col) in diag1 or (row + col) in diag2:
            return False

        # Добавляем координаты в множества для дальнейшей проверки
        rows.add(row)
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

    return True

# Функция для генерации случайной расстановки ферзей
def generate_random_queens() -> List[Tuple[int, int]]:
    """
    Генерирует случайную расстановку ферзей на доске 8x8.
    Каждый ферзь имеет уникальную строку, но случайный столбец.
    :return: Список из 8 пар чисел — координаты ферзей.
    """
    columns = list(range(1, 9))  # Столбцы от 1 до 8
    random.shuffle(columns)  # Перемешиваем столбцы случайным образом

    # Каждому ферзю назначаем уникальную строку (от 1 до 8) и случайный столбец
    queens = [(i + 1, columns[i]) for i in range(8)]
    return queens

# Функция для нахождения 4 успешных расстановок
def find_successful_arrangements() -> List[List[Tuple[int, int]]]:
    successful_arrangements = []
    attempts = 0

    while len(successful_arrangements) < 4:
        queens = generate_random_queens()
        if is_safe(queens):
            successful_arrangements.append(queens)
        attempts += 1
        if attempts > 1000:  # Ограничиваем количество попыток для предотвращения бесконечного цикла
            break

    return successful_arrangements

# Пример использования
successful_queens_arrangements = find_successful_arrangements()

# Вывод успешных расстановок
for i, arrangement in enumerate(successful_queens_arrangements, 1):
    print(f"Успешная расстановка {i}: {arrangement}")
