"""
Задача 2.1

Создайте в переменной data список значений разных типов, перечислив их через запятую внутри квадратных скобок.
Для каждого элемента в цикле выведите: 
Порядковый номер начиная с единицы.
Значение
Адрес в памяти 
Размер в памяти 
Хэш объекта (только для тех типов, которые поддерживают хэширование)
Результат проверки на целое число только если он положительный 
Результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

from sys import getsizeof
from typing import Hashable

# Вариант 1
print("Вариант 1\n")
data1 = [42, 3.14, "Hello, World!", True, [1, 2, 3, 4, 5], (10, 20, 30), {"ключ1": "значение1", "ключ2": "значение2"}, {1, 2, 3, 4, 5}, 42, "Hello, World!"]

for i, value in enumerate(data1, 1):  # Порядковый номер начиная с единицы
    print(f"Порядковый номер: {i}")  # Порядковый номер начиная с единицы
    print(f"Значение: {value}")      # Значение
    print(f"Адрес в памяти: {id(value)}")  # Адрес в памяти
    print(f"Размер в памяти: {value.__sizeof__()}") # Размер в памяти
    try:
        print(f"Хэш объекта: {hash(value)}") # Хэш объекта
    except TypeError:  # Обработка исключения
        print("Хэш объекта: Невозможно вычислить хэш для данного типа данных")
    
    if isinstance(value, int) and value > 0:  # Проверка на целое число
        print(f"Результат проверки на целое число: {True}")  # Результат проверки на целое число
    if isinstance(value, str):  # Проверка на строку
        print(f"Результат проверки на строку: {True}") # Результат проверки на строку
    print()

# Вариант 2
print("Вариант 2\n")
data2 = [1, "Строка", 5.11, [1, 2, 3], 5.11, 1]

for i in range(len(data2)):
    print(i+1, end="\t ")  # Порядковый номер начиная с единицы
    print(data2[i], end="\t ")  # Значение
    print(id(data2[i]), end="\t ")  # Адрес в памяти
    print(getsizeof(data2[i]), end="\t ")  # Размер в памяти
    if isinstance(data2[i], Hashable):  # Проверка на хэшируемость
        print(hash(data2[i]), end="\t ")  # Хэш объекта
    else:
        print("Невозможно вычислить хэш", end="\t ")

    if isinstance(data2[i], int) and data2[i] > 0:  # Проверка на целое число
        print("Целое", end="\t ")

    if isinstance(data2[i], str):  # Проверка на строку
        print("Строка", end="\t ")

    if data2.count(data2[i]) > 1:  # Проверка на повторяющиеся элементы
        print("Повторяющийся элемент", end="\t ")
        
    if type(data2[i]) == float:
        print("Дробное число", end="\t ")

    print()  # Переход на новую строку после вывода всех данных
