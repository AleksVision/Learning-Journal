import json
import csv
import pickle
from typing import List, Dict, Any

def save_to_json(data: List[Dict[str, Any]], filename: str) -> None:
    """Сохраняет данные в JSON формат."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def save_to_csv(data: List[Dict[str, Any]], filename: str) -> None:
    """Сохраняет данные в CSV формат."""
    if not data:
        return
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data: List[Dict[str, Any]], filename: str) -> None:
    """Сохраняет данные в Pickle формат."""
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
