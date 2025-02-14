""" 
Задача 2.1

Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
строковое представление. Функцию hex используйте для проверки своего результата.
"""
number = int(input("Введите число: "))

# Решение 1
print(f"Решение 1: {hex(number)[2:]}")
result_hex = ''                 # Результат в шестнадцатеричной системе
hex_digits = "0123456789ABCDEF" # Символы для шестнадцатеричной системы
temp_number = number            # Временное хранение числа

while temp_number > 0:
    remainder = temp_number % 16
    result_hex = hex_digits[remainder] + result_hex
    temp_number //= 16

# Проверка через встроенную функцию
print(f"Реализация: {result_hex}")
print(f"Проверка через hex(): {hex(number)[2:]}")

# Решение 2 
print(f"Решение 2: {hex(number)[2:]}")
# Используем функцию

def decimal_to_hex(number):
    """
    Преобразует десятичное число в шестнадцатеричное.
    
    Args:
        number (int): Десятичное число для преобразования
    
    Returns:
        str: Строка, представляющая число в шестнадцатеричной системе
    """
    # Константы
    BASE_HEX = 16
    HEX_DIGITS = "0123456789ABCDEF"  # Символы для шестнадцатеричной системы
    
    # Обработка отрицательных чисел
    if number < 0:
        return f"-{decimal_to_hex(abs(number))}"
    # Обработка нуля
    elif number == 0:
        return "0"
    
    result_hex = ''
    temp_number = number
    
    # Преобразование числа в шестнадцатеричную систему
    while temp_number > 0:
        # Получаем остаток от деления на 16
        remainder = temp_number % BASE_HEX
        # Добавляем соответствующий символ в начало строки
        result_hex = HEX_DIGITS[remainder] + result_hex
        # Целочисленное деление на 16
        temp_number //= BASE_HEX
    
    return result_hex

def main():
    try:
        # Получаем число от пользователя
        number = int(input("Введите целое число: "))
        
        # Получаем результат  функции
        custom_result = decimal_to_hex(number)
        print(f"Функция: {custom_result}")
        
        # Получаем результат встроенной функции hex() (без префикса 0x)
        builtin_result = hex(number)[2:] if number >= 0 else hex(number)[3:]
        print(f"Встроенная функция hex(): {builtin_result}")
        
        # Проверяем совпадение результатов
        if custom_result.upper() == builtin_result.upper():
            print("Результаты совпадают!")
        else:
            print("Ошибка: результаты не совпадают")
            
    except ValueError:
        print("Ошибка: введите корректное целое число")

if __name__ == "__main__":
    main()