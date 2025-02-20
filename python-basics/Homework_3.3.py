""" 
Задача 3
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
"""
# Решение 
from itertools import combinations

# Создаем словарь со списком вещей и их массой
items = {
    "Палатка": 3.5,
    "Спальный мешок": 2.0,
    "Фонарик": 0.3,
    "Нож": 0.2,
    "Аптечка": 1.0,
    "Вода": 1.5,
    "Еда": 2.5,
    "Карта": 0.1,
    "Компас": 0.1,
    "Запасная одежда": 1.0
}

# Максимальная грузоподъёмность рюкзака
max_weight = 10.0

# Создаем список для хранения всех возможных комбинаций
item_list = list(items.items())
all_combinations = []

# Генерируем все возможные комбинации вещей
for r in range(1, len(item_list) + 1):
    for combination in combinations(item_list, r):
        total_weight = sum(item[1] for item in combination)
        if total_weight <= max_weight:
            all_combinations.append((combination, round(total_weight, 2)))

# Выводим все возможные варианты комплектации рюкзака
print(f"Все возможные варианты комплектации рюкзака при максимальной грузоподъёмности {max_weight} кг:")
for comb, weight in all_combinations:
    items_str = ", ".join(f"{item[0]} ({item[1]} кг)" for item in comb)
    print(f"Комплектация: {items_str} | Общий вес: {weight} кг")
