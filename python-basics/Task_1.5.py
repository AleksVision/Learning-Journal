   
"""
Задача: Вывести в консоль таблицу умножения как в школьной тетради от 2*2 до 9*10.
"""

# Печать заголовка таблицы
print("Таблица умножения от 2*2 до 9*10\n")  # Печатаем заголовок таблицы

# Функция для печати строки таблицы умножения
def print_multiplication_row(start, end, row): # start - начальный множитель, end - конечный множитель, row - строка таблицы
    for i in range(start, end + 1):            # Перебираем множители от start до end включительно
        print(f"{i} * {row} = {i * row:<2} ", end="\t")   # Печатаем произведение с выравниванием по левому краю
    print()                                               # Переходим на новую строку

# Внешний цикл для строк (от 1 до 10)
for i in range(1, 11):                                # Перебираем строки от 1 до 10
    # Печатаем первый ряд таблицы (с множителями от 2 до 5)
    print_multiplication_row(2, 5, i)                # Печатаем строку таблицы с множителями от 2 до 5
print()  # Пустая строка для разделения между двумя рядами

# Внешний цикл для строк (от 1 до 10)
for i in range(1, 11):                               # Перебираем строки от 1 до 10
    # Печатаем второй ряд таблицы (с множителями от 6 до 9)
    print_multiplication_row(6, 9, i)                 # Печатаем строку таблицы с множителями от 6 до 9

# Второй вариант решения задачи

# Печать заголовка таблицы
print("Таблица умножения от 2*2 до 9*10\n")

# Первая часть таблицы (от 2 до 5)
for i in range(2, 11): # Перебираем строки от 2 до 10
    for j in range(2, 6): # Перебираем множители от 2 до 5
        print(f"{j} * {i} = {j * i:2} ", end="\t") # Печатаем произведение с выравниванием по левому краю
    print()

print()  # Пустая строка для разделения частей таблицы

# Вторая часть таблицы (от 6 до 9)
for i in range(2, 11): # Перебираем строки от 2 до 10
    for j in range(6, 10): # Перебираем множители от 6 до 9
        print(f"{j} * {i} = {j * i:2} ", end="\t")  # Печатаем произведение с выравниванием по левому краю
    print()
