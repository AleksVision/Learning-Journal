'''
Задание 5.3
Создайте функцию генератор чисел Фибоначчи https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
(от 0 до n) с использованием yield.
Пример:
fib = fibonacci(10)
for i in fib:
    print(i)
# Вывод:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
'''
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

# Пример использования функции
fib = fibonacci(10)
for i in fib:
    print(i)
