import json
import os

def text_to_json(name='res.txt'):
    """
    Конвертирует текстовый файл в JSON.
    
    Args:
        name (str): Имя входного файла
    """
    try:
        # Получаем абсолютный путь к файлу
        current_dir = os.path.dirname(os.path.abspath(__file__))
        input_file = os.path.join(current_dir, name)
        output_file = os.path.join(current_dir, 'res.json')
        
        # Проверяем существование файла
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Файл {name} не найден в директории {current_dir}")
        
        # Открытие исходного файла для чтения
        with open(input_file, 'r', encoding='utf-8') as f:
            res_list = [line.strip().capitalize() for line in f]
        
        # Открытие файла для записи результата
        with open(output_file, 'w', encoding='utf-8') as f2:
            json.dump(res_list, f2, indent=4, ensure_ascii=False)
            
        print(f"Файл успешно конвертирован в {output_file}")
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    text_to_json()

