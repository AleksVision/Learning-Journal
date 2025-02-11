# task_1.py

"""
Задача 1: Приветствие пользователя
Напишите программу, которая запрашивает имя пользователя и выводит приветствие.
"""

def greet_user():
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}! Добро пожаловать в мир Python!")

if __name__ == "__main__":
    greet_user()

# Пример работы программы:
# Введите ваше имя: Alice
# Привет, Alice! Добро пожаловать в мир Python!

# Запрашиваем числа у пользователя
# Запрашиваем числа у пользователя
n = int(input("Введите число n: "))   
e = int(input("Введите число e: "))   

count = 2       # Начинаем с 2, так как число четное
sum_1 = 0       # Сумма делителей

while count <= n:  # Цикл продолжается, пока count меньше или равно n
    if count % e == 0:  # Если число делится на e, то пропускаем его
        count += 2     # Увеличиваем число на 2
        continue       # Пропускаем число
    sum_1 += count     # Суммируем делители
    print(sum_1)       # Выводим промежуточную сумму делителей
    count += 2         # Увеличиваем число на 2

print("Итоговая сумма делителей:", sum_1)  # Выводим итоговую сумму делителей
