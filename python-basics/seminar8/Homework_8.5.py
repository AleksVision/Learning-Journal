'''
Задание 8.5
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
'''
import json
import pickle
import os
from typing import List

def json_to_pickle(directory: str) -> List[str]:
    """
    Ищет все JSON файлы в указанной директории и сохраняет их содержимое 
    в виде одноименных pickle файлов.
    
    Args:
        directory (str): Путь к директории с JSON файлами
    
    Returns:
        List[str]: Список обработанных файлов
    """
    processed_files = []
    
    try:
        # Получаем абсолютный путь к директории
        abs_directory = os.path.abspath(directory)
        
        if not os.path.isdir(abs_directory):
            raise NotADirectoryError(f"Директория '{directory}' не существует!")

        # Проходим по всем файлам в директории
        for filename in os.listdir(abs_directory):
            if filename.endswith('.json'):
                json_filepath = os.path.join(abs_directory, filename)
                
                # Чтение JSON файла
                try:
                    with open(json_filepath, 'r', encoding='utf-8') as f_json:
                        data = json.load(f_json)
                    
                    # Формируем имя для pickle файла
                    pickle_filepath = os.path.splitext(json_filepath)[0] + '.pkl'
                    
                    # Сохраняем данные в pickle файл
                    with open(pickle_filepath, 'wb') as f_pickle:
                        pickle.dump(data, f_pickle)
                    
                    processed_files.append(filename)
                    print(f"✅ {filename} -> {os.path.basename(pickle_filepath)}")
                
                except json.JSONDecodeError as e:
                    print(f"❌ Ошибка чтения {filename}: {e}")
                except Exception as e:
                    print(f"❌ Ошибка обработки {filename}: {e}")
        
        return processed_files
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return processed_files

if __name__ == "__main__":
    # Используем текущую директорию
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"Поиск JSON файлов в: {current_dir}")
    processed = json_to_pickle(current_dir)
    
    if processed:
        print(f"\nОбработано файлов: {len(processed)}")
        print("Список обработанных файлов:")
        for file in processed:
            print(f"- {file}")
    else:
        print("\nJSON файлы не найдены")
