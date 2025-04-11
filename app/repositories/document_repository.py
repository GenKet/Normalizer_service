from sqlalchemy.orm import Session
from app.db.models import ProcessedDocumentDB


def create_processed_document(db: Session, original: dict, normalized: dict) -> ProcessedDocumentDB:
    """
    Сохраняет обработанный документ в базу данных.
    
    :param db: SQLAlchemy сессия
    :param original: Исходные данные документа
    :param normalized: Нормализованные данные документа
    :return: Сохранённая сущность документа
    """
    db_document = ProcessedDocumentDB(original_data=original, normalized_data=normalized)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document
