import os
from file_utils import process_directory, save_to_json, save_to_csv, save_to_pickle

def test_file_utils():
    # Текущая директория
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Сканируем директорию
    files_info = process_directory(current_dir)
    
    # Сохраняем результаты
    save_to_json(files_info, 'files_info.json')
    save_to_csv(files_info, 'files_info.csv')
    save_to_pickle(files_info, 'files_info.pkl')
    
    print("✅ Файлы успешно обработаны!")

if __name__ == "__main__":
    test_file_utils()
