import re

def normalize_field(key: str, value):
    """
    Выполняет нормализацию отдельных полей:
    - Если значение является строкой, убираются лишние пробелы.
    - При обнаружении суммы (например, "10000,00 рублей") производится замена запятой и удаление текстовой части.
    - Рекурсивно обрабатываются списки и вложенные словари.
    """
    if isinstance(value, str):
        normalized_value = value.strip()
        if re.search(r'\d+,\d+\s*руб', normalized_value, re.IGNORECASE):
            normalized_value = normalized_value.replace(",", ".")
            normalized_value = normalized_value.replace("рублей", "").strip()
        return normalized_value
    elif isinstance(value, list):
        return [normalize_field(key, item) for item in value]
    elif isinstance(value, dict):
        return normalize_document(value)
    return value

def normalize_document(document: dict) -> dict:
    """
    Рекурсивно нормализует все поля в документе.
    """
    normalized_data = {}
    for key, value in document.items():
        normalized_data[key] = normalize_field(key, value)
    return normalized_data
