# Python для начинающих: Полное руководство

## Содержание
1. [Установка Python](#установка-python)
2. [Виртуальное окружение и pip](#виртуальное-окружение-и-pip)
3. [Основы синтаксиса Python](#основы-синтаксиса-python)
4. [Рекомендации по оформлению кода](#рекомендации-по-оформлению-кода)
5. [Ветвящиеся алгоритмы](#ветвящиеся-алгоритмы)
6. [Циклы в Python](#циклы-в-python)
7. [Частые ошибки и их решения](#частые-ошибки-и-их-решения)

## Установка Python

### Для MacOS
1. Установка через Homebrew (рекомендуемый способ):
```bash
# Установка Homebrew (если еще не установлен)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Установка Python
brew install python
```

2. Проверка установки:
```bash
python3 --version
```

### Настройка PATH (для MacOS)
Добавьте в ~/.zshrc или ~/.bash_profile:
```bash
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```

После добавления строки выполните:
```bash
source ~/.zshrc  # или source ~/.bash_profile
```

## Виртуальное окружение и pip

### Что такое виртуальное окружение?
Виртуальное окружение - это изолированное пространство, где вы можете устанавливать и управлять зависимостями для конкретного проекта, не влияя на другие проекты или системный Python.

### Создание и управление виртуальным окружением
```bash
# Создание окружения
python3 -m venv myenv

# Активация окружения
# Для MacOS/Linux:
source myenv/bin/activate

# Для Windows:
# myenv\Scripts\activate

# Проверка активации
which python  # должен показывать путь к Python в вашем виртуальном окружении

# Деактивация окружения
deactivate
```

### Структура виртуального окружения
```
myenv/
├── bin/               # Исполняемые файлы
├── include/           # Заголовочные файлы C
├── lib/              # Библиотеки Python
└── pyvenv.cfg        # Конфигурационный файл
```

### Продвинутая работа с pip
```bash
# Обновление pip
pip install --upgrade pip

# Установка определенной версии пакета
pip install package_name==1.0.0

# Установка последней совместимой версии
pip install "package_name>=1.0.0,<2.0.0"

# Просмотр установленных пакетов
pip list

# Проверка устаревших пакетов
pip list --outdated

# Создание requirements.txt с указанием версий
pip freeze > requirements.txt

# Установка зависимостей из requirements.txt
pip install -r requirements.txt
```

## Основы синтаксиса Python

### Переменные и типы данных
```python
# Основные типы данных с примерами
name = "John"  # строка (str)
age = 25      # целое число (int)
height = 1.75 # число с плавающей точкой (float)
is_student = True  # булево значение (bool)

# Сложные типы данных
my_list = [1, 2, 3]        # список (изменяемый)
my_tuple = (1, 2, 3)       # кортеж (неизменяемый)
my_dict = {"key": "value"} # словарь
my_set = {1, 2, 3}        # множество

# Преобразование типов
str_number = "123"
number = int(str_number)  # преобразование строки в число
float_number = float(str_number)  # преобразование строки в число с плавающей точкой
```

### Работа со строками
```python
# Форматирование строк
name = "Alice"
age = 25

# f-строки (рекомендуемый способ)
message = f"Привет, меня зовут {name} и мне {age} лет"

# метод format()
message = "Привет, меня зовут {} и мне {} лет".format(name, age)

# Методы строк
text = "  Python Programming  "
print(text.strip())         # убирает пробелы в начале и конце
print(text.lower())         # переводит в нижний регистр
print(text.upper())         # переводит в верхний регистр
print(text.replace("P", "J")) # заменяет символы
```

## Ветвящиеся алгоритмы

### Продвинутые условные операторы
```python
# Сложные условия
age = 25
income = 50000
experience = 3

if (age >= 25 and income >= 50000) or experience > 5:
    print("Кредит одобрен")
elif 21 <= age < 25 and income >= 30000:
    print("Требуется дополнительная проверка")
else:
    print("Кредит не одобрен")

# Использование match (Python 3.10+)
def analyze_type(value):
    match value:
        case str():
            return "Это строка"
        case int() | float():
            return "Это число"
        case list():
            return "Это список"
        case _:
            return "Неизвестный тип"

# Вложенные условия с обработкой исключений
def divide_numbers(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Оба аргумента должны быть числами")
        if b == 0:
            raise ZeroDivisionError("Деление на ноль недопустимо")
        return a / b
    except (TypeError, ZeroDivisionError) as e:
        return f"Ошибка: {e}"
```

## Циклы в Python

### Продвинутые примеры использования циклов
```python
# Вложенные циклы с условиями
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Поиск элементов в матрице
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 == 0:
            print(f"Четное число {matrix[i][j]} находится в позиции [{i}][{j}]")

# Цикл с несколькими условиями выхода
def find_number(numbers, target):
    i = 0
    while i < len(numbers):
        if numbers[i] == target:
            return f"Число {target} найдено на позиции {i}"
        elif numbers[i] > target:
            return f"Число {target} не найдено, поиск прекращен на позиции {i}"
        i += 1
    return f"Число {target} не найдено в списке"

# Использование else с циклами
def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} делится на {i}")
            break
    else:
        print(f"{n} является простым числом")
        return True
    return False

# Генераторы списков с условиями
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers if x % 2 == 0]  # квадраты четных чисел
```

## Частые ошибки и их решения

### Синтаксические ошибки
```python
# ❌ Неправильно: отсутствие двоеточия после if
if x > 5
    print(x)

# ✅ Правильно
if x > 5:
    print(x)

# ❌ Неправильно: неправильные отступы
def my_function():
print("Hello")  # отсутствует отступ

# ✅ Правильно
def my_function():
    print("Hello")
```

### Логические ошибки
```python
# ❌ Неправильно: бесконечный цикл
while True:
    print("Hello")

# ✅ Правильно
counter = 0
while counter < 5:
    print("Hello")
    counter += 1

# ❌ Неправильно: неправильное сравнение строк
if "5" == 5:
    print("Равны")

# ✅ Правильно
if int("5") == 5:
    print("Равны")
```

### Ошибки с типами данных
```python
# ❌ Неправильно: сложение строки и числа
result = "123" + 456

# ✅ Правильно
result = int("123") + 456  # или str("123") + str(456)

# ❌ Неправильно: индексация строки
text = "Python"
text[0] = "J"  # строки неизменяемы!

# ✅ Правильно
text = "Python"
new_text = "J" + text[1:]
```

### Ошибки при работе с файлами
```python
# ❌ Неправильно: файл не закрывается
file = open("example.txt", "r")
content = file.read()

# ✅ Правильно: использование контекстного менеджера
with open("example.txt", "r") as file:
    content = file.read()
```

### Распространенные исключения и их обработка
```python
def safe_operations():
    try:
        # IndexError
        list_example = [1, 2, 3]
        print(list_example[10])
    except IndexError as e:
        print(f"Ошибка индекса: {e}")

    try:
        # KeyError
        dict_example = {"a": 1}
        print(dict_example["b"])
    except KeyError as e:
        print(f"Ошибка ключа: {e}")

    try:
        # TypeError
        result = "2" + 2
    except TypeError as e:
        print(f"Ошибка типа: {e}")

    try:
        # ValueError
        number = int("abc")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
```
