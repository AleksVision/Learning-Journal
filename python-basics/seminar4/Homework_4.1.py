def transpose_matrix(matrix):
    # Транспонирование матрицы с использованием zip
    return [list(row) for row in zip(*matrix)]

# Исходная матрица
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Транспонированная матрица
transposed = transpose_matrix(matrix)

# Вывод транспонированной матрицы
for row in transposed:
    print(row)
