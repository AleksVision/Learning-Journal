def create_dict(**kwargs):
    result = {}
    
    for key, value in kwargs.items():
        # Проверяем, является ли значение хешируемым
        try:
            hash(value)  # Если значение хешируемо, оно пройдет проверку
            result[value] = key
        except TypeError:
            # Если возникает ошибка TypeError (значение не хешируемо), используем строковое представление
            result[str(value)] = key
    
    return result

# Пример использования функции:
result = create_dict(a=1, b=[1, 2, 3], c="hello", d={1, 2})
print(result)
