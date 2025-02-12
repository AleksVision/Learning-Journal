"""Задание 3

3. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randint
hum = randint (LOWER_LIMIT, UPPER_LIMIT) 
"""
from random import randint

# Генерация случайного числа от 0 до 1000
LOWER_LIMIT = 0  # Нижний предел
UPPER_LIMIT = 1000  # Верхний предел
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT) # Загаданное число

print("Я загадал число от 0 до 1000. Попробуйте угадать его за 10 попыток.")

# Количество попыток
attempts = 10

# Цикл для угадывания числа
for attempt in range(1, attempts + 1):
    guess = int(input(f"Попытка {attempt}: Введите ваше предположение: "))
    
    if guess < secret_number:
        print("Больше")
    elif guess > secret_number:
        print("Меньше")
    else:
        print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток.")
        break
else:
    print(f"К сожалению, вы не угадали число. Загаданное число было {secret_number}.")
