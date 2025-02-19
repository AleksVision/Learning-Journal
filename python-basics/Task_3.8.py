""" 
Задача 8
Три друга взяли вещи в поход. Сформируйте словарь, где ключ имя друга, а значение кортеж из вещей. Ответьте на вопросы: 
Какие вещи взяли все три друга?
Какие вещи уникальны, есть только у одного друга?
Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует?
Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

# Решение 1
# Создаем словарь с вещами друзей
friends_dict = {
    "Антон": ("палатка", "спальный мешок", "фонарик", "нож", "сигареты"),
    "Борис": ("спальный мешок", "фонарик", "нож", "аптечка", "сигареты"),
    "Виктор": ("спальный мешок", "фонарик", "нож", "карта", "компас")
}

# Вещи, которые взяли все три друга
all_items = set(friends_dict["Антон"])
for items in friends_dict.values():
    all_items &= set(items)
print("Вещи, которые взяли все три друга:", ', '.join(all_items))

# Уникальные вещи, есть только у одного друга
unique_items = set()
for friend, items in friends_dict.items():
    other_items = set(item for f, i in friends_dict.items() if f != friend for item in i)
    unique_items |= set(items) - other_items
print("Уникальные вещи, которые есть только у одного друга:", ', '.join(unique_items))

# Вещи, которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
items_excluding_one = {}
for friend, items in friends_dict.items():
    other_friends = {f: i for f, i in friends_dict.items() if f != friend}
    common_items = set.intersection(*[set(i) for i in other_friends.values()])
    exclusive_items = common_items - set(items)
    for item in exclusive_items:
        if item not in items_excluding_one:
            items_excluding_one[item] = []
        items_excluding_one[item].append(friend)

if items_excluding_one:
    print("Вещи, которые есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует:")
    for item, friends in items_excluding_one.items():
        print(f"Вещь '{item}' есть у всех друзей кроме {', '.join(friends)}.")
else:
    print("Нет таких вещей, которые есть у всех друзей кроме одного.")

# Решение 2
# Словарь с вещами друзей
dic_things = {
    "Александр": {"палатка", "спальный мешок", "фонарик", "нож", "сигареты"},
    "Борис": {"спальный мешок", "фонарик", "нож", "аптечка", "сигареты"},
    "Виктор": {"спальный мешок", "фонарик", "нож", "карта", "компас"},
}

# Все вещи всех друзей
all_items = set().union(*dic_things.values())

# Вещи, которые есть у всех друзей
common_items = set.intersection(*dic_things.values())

# Подсчет количества владельцев для каждой вещи
item_count = {item: sum(item in things for things in dic_things.values()) for item in all_items}

# Вещи, которые уникальны (есть только у одного друга)
unique_items = {item for item, count in item_count.items() if count == 1}

# Вещи, которых не хватает только одному другу
missing_items = {item: [friend for friend, things in dic_things.items() if item not in things] for item, count in item_count.items() if count == len(dic_things) - 1}

# Вывод результатов
print("Вещи, которые взяли все:", ", ".join(common_items))

print("Уникальные вещи (есть только у одного друга):")
for friend, things in dic_things.items():
    unique = unique_items & things
    if unique:
        print(f"  {friend}: {', '.join(unique)}")

print("Вещи, которые есть у всех кроме одного:")
for item, missing_friends in missing_items.items():
    print(f"  {item} отсутствует у {missing_friends[0]}")
