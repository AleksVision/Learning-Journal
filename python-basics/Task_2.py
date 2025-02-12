"""Создайте несколько переменных разных типов
Проверьте к какому типу относится созданные переменные с помощью функции type()"""

# Создание переменных разных типов
integer_var = 42  # целое число
float_var = 3.14 # число с плавающей точкой
string_var = "Hello, World!" # строка
boolean_var = True # логическое значение
list_var = [1, 2, 3, 4, 5] # список
tuple_var = (10, 20, 30) # кортеж
dict_var = {"ключ1": "значение1", "ключ2": "значение2"} # словарь
set_var = {1, 2, 3, 4, 5} # множество

# Проверка типов переменных
print(f"integer_var = {integer_var}, тип: {type(integer_var)}")
print(f"float_var = {float_var}, тип: {type(float_var)}")
print(f"string_var = '{string_var}', тип: {type(string_var)}")
print(f"boolean_var = {boolean_var}, тип: {type(boolean_var)}")
print(f"list_var = {list_var}, тип: {type(list_var)}")
print(f"tuple_var = {tuple_var}, тип: {type(tuple_var)}")
print(f"dict_var = {dict_var}, тип: {type(dict_var)}")
print(f"set_var = {set_var}, тип: {type(set_var)}")
