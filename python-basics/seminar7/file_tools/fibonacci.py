# file_tools/fibonacci.py
from typing import Generator

def fibonacci(n: int) -> Generator[int, None, None]:
    """
    Генератор чисел Фибоначчи от 0 до n.
    
    :param n: Максимальное значение числа Фибоначчи.
    :return: Генератор чисел Фибоначчи.
    """
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
