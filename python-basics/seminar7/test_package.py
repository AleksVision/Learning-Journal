from file_tools import get_files, batch_rename_files, is_safe, fibonacci

def test_package():
    print("=== Тестирование пакета file_tools ===")
    
    # Тест поиска файлов
    files = get_files(".", ".py", True)
    print(f"\nНайдено Python файлов: {len(files)}")
    
    # Тест чисел Фибоначчи
    print("\nПервые 10 чисел Фибоначчи:")
    for num in list(fibonacci(100))[:10]:
        print(num, end=" ")

if __name__ == "__main__":
    test_package()
