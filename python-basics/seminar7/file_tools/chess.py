# file_tools/chess.py
from typing import List, Tuple

def is_safe(queens: List[Tuple[int, int]]) -> bool:
    """
    Проверяет, не бьют ли друг друга ферзи, расставленные на доске.
    
    :param queens: Список из 8 пар чисел, где каждая пара — это координаты ферзя (строка, столбец).
    :return: True, если ферзи не бьют друг друга, иначе False.
    """
    rows = set()
    cols = set()
    diag1 = set()
    diag2 = set()

    for row, col in queens:
        if row in rows or col in cols or (row - col) in diag1 or (row + col) in diag2:
            return False

        rows.add(row)
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)

    return True
