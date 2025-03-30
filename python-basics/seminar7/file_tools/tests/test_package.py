from file_tools import get_files, batch_rename_files, is_safe, fibonacci

def test_all_features():
    # 1. Тест поиска файлов
    print("\n=== Тест поиска файлов ===")
    files = get_files(".", ".py", True)
    print(f"Найдено Python файлов: {len(files)}")

    # 2. Тест переименования
    print("\n=== Тест переименования ===")
    batch_rename_files(
        directory="test_files",
        base_name="_new",
        num_digits=3,
        old_extension=".txt",
        new_extension="pdf",
        name_range=(1, 4)
    )

    # 3. Тест расстановки ферзей
    print("\n=== Тест расстановки ферзей ===")
    queens = [(1, 1), (2, 5), (3, 8), (4, 6),
             (5, 3), (6, 7), (7, 2), (8, 4)]
    print(f"Расстановка корректна: {is_safe(queens)}")

    # 4. Тест Фибоначчи
    print("\n=== Тест чисел Фибоначчи ===")
    for num in fibonacci(50):
        print(num, end=" ")
    print()

if __name__ == "__main__":
    test_all_features()
