""" 
Пользователь вводит числа от 1 до 999. Используя операции с числами сообщите, что 
введено: цифра, двухзначное число или трехзначное число.
Для цифры верните ее в квадрат, например 5 - 25.
Для двухзначного числа произведение цифр, например 30 - 0.
Для трехзначного числа его зеркальное отражение, например 520 - 25.
Если числа не из диапазона, запросите новое число.
Откажитесь от магических чисел.
В коде должен быть один input и не более одного print.
"""

# Определения границ для лучшей читаемости и отказа от магических чисел
MIN_VALUE = 1    # Минимальное значение
MAX_VALUE = 999  # Максимальное значение

while True:  # Бесконечный цикл
    a = int(input("Введите число (от 1 до 999): "))  # Запрашиваем число у пользователя
    
    if a < MIN_VALUE or a > MAX_VALUE:  # Проверяем, что число в диапазоне
        print("Число должно быть от 1 до 999. Пожалуйста, введите число еще раз.")
        continue
    
    if a < 10:
        result = f"Это цифра. Квадрат числа: {a ** 2}"  # Квадрат числа
    elif a < 100:
        result = f"Это двухзначное число. Произведение цифр: {(a // 10) * (a % 10)}"  # Произведение цифр
    else:
        result = f"Это трехзначное число. Зеркальное отражение: {str(a)[::-1]}"  # Зеркальное отражение числа
    
    # Выводим результат только один раз в конце
    print(result)
    break

# Примеры работы со строками

s = "1234567890"

print(s[::2])  # 13579  - выводит каждый второй символ
print(s[1::2])  # 24680 - выводит каждый второй символ, начиная со второго
print(s[::-1])  # 0987654321 - выводит строку в обратном порядке
print(s[-3:])  # 890 - выводит последние три символа
print(s[:-6])  # 1234 - выводит строку, кроме последних шести символов
print(s[-1:-10:-1])  # 098765432 - выводит последние девять символов в обратном порядке