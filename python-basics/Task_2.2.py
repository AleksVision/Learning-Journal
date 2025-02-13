"""
Двойное и восьмеричное представление числа
"""
number = int(input("Введите число: "))

# Двоичное представление
BASE_BIN = 2
print(bin(number))  # Встроенная функция для отображения числа в двоичной системе
result_bin = ''
temp_number = number
while temp_number > 0:
    result_bin = str(temp_number % BASE_BIN) + result_bin
    temp_number //= BASE_BIN
print(result_bin)

# Восьмеричное представление
BASE_OCT = 8
print(oct(number))  # Встроенная функция для отображения числа в восьмеричной системе
result_oct = ''
temp_number = number
while temp_number > 0:
    result_oct = str(temp_number % BASE_OCT) + result_oct
    temp_number //= BASE_OCT
print(result_oct)
