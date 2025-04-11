from app.utils import normalization
from app.repositories import document_repository

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Рекурсивное объединение двух словарей.
    Если ключ присутствует в обоих словарях и значения являются словарями – выполняется рекурсивное слияние.
    Если значения не являются словарями, то объединяются в список с уникальными значениями.
    """
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts(result[key], value)
            else:
                if not isinstance(result[key], list):
                    result[key] = [result[key]]
                if value not in result[key]:
                    result[key].append(value)
        else:
            result[key] = value
    return result

def process_documents(data: dict, db) -> dict:
    """
    Обработка документов:
      - Нормализация каждого документа.
      - Объединение исходных данных из нескольких документов.
      - Сохранение обработанного результата в базу данных.
      
    :param data: Входной словарь документов
    :param db: SQLAlchemy сессия базы данных (dependency injection)
    :return: Словарь с исходными и нормализованными данными.
    """
    if not isinstance(data, dict):
        raise ValueError("Входные данные должны быть формата словаря")

    merged_original = {}
    merged_normalized = {}

    for doc_key, doc_content in data.items():
        if not isinstance(doc_content, dict):
            continue 

        normalized_doc = normalization.normalize_document(doc_content)

        merged_original = merge_dicts(merged_original, {doc_key: doc_content})

        merged_normalized = merge_dicts(merged_normalized, {doc_key: normalized_doc})

    document_repository.create_processed_document(db, merged_original, merged_normalized)
    
    return {"original": merged_original, "normalized": merged_normalized}
