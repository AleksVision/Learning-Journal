''' 
Задание 2.2

Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте 
модуль fractions
'''

from fractions import Fraction

def gcd(a: int, b: int) -> int:
    """
    Находит наибольший общий делитель двух чисел
    """
    while b:
        a, b = b, a % b
    return abs(a)

def simplify_fraction(numerator: int, denominator: int) -> tuple:
    """
    Сокращает дробь, возвращая кортеж (числитель, знаменатель)
    """
    if denominator == 0:
        raise ValueError("Знаменатель не может быть равен нулю")
        
    divisor = gcd(numerator, denominator)
    return (numerator // divisor, denominator // divisor)

def parse_fraction(fraction_str: str) -> tuple:
    """
    Преобразует строку вида "a/b" в кортеж чисел (a, b)
    """
    try:
        numerator, denominator = map(int, fraction_str.split('/'))
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")
        return (numerator, denominator)
    except ValueError as e:
        if "not enough values to unpack" in str(e):
            raise ValueError("Неверный формат дроби. Используйте формат 'a/b'")
        raise

def add_fractions(frac1: tuple, frac2: tuple) -> tuple:
    """
    Складывает две дроби и возвращает сокращенный результат
    """
    n1, d1 = frac1
    n2, d2 = frac2
    # Находим общий знаменатель и складываем числители
    new_numerator = n1 * d2 + n2 * d1
    new_denominator = d1 * d2
    return simplify_fraction(new_numerator, new_denominator)

def multiply_fractions(frac1: tuple, frac2: tuple) -> tuple:
    """
    Перемножает две дроби и возвращает сокращенный результат
    """
    n1, d1 = frac1
    n2, d2 = frac2
    return simplify_fraction(n1 * n2, d1 * d2)

def fraction_to_str(fraction: tuple) -> str:
    """
    Преобразует кортеж (числитель, знаменатель) в строку вида "a/b"
    """
    return f"{fraction[0]}/{fraction[1]}"

def main():
    try:
        # Получаем дроби от пользователя
        frac1_str = input("Введите первую дробь (в формате a/b): ")
        frac2_str = input("Введите вторую дробь (в формате a/b): ")

        # Разбираем строки в кортежи
        frac1 = parse_fraction(frac1_str)
        frac2 = parse_fraction(frac2_str)

        # Вычисляем результаты функциями
        sum_result = add_fractions(frac1, frac2)
        prod_result = multiply_fractions(frac1, frac2)

        # Проверяем результаты с помощью модуля fractions
        f1 = Fraction(frac1[0], frac1[1])
        f2 = Fraction(frac2[0], frac2[1])
        
        print("\nРезультаты:")
        print(f"Сумма дробей:")
        print(f"Функция: {fraction_to_str(sum_result)}")
        print(f"Проверка через fractions: {f1 + f2}")
        
        print(f"\nПроизведение дробей:")
        print(f"Функция: {fraction_to_str(prod_result)}")
        print(f"Проверка через fractions: {f1 * f2}")

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()