from typing import Any, Dict
from pydantic import BaseModel, RootModel

class DocumentInput(RootModel[Dict[str, Dict[str, Any]]]):
    """
    Модель для входных документов.
    Ожидается словарь, где ключ – идентификатор документа, значение – его содержимое.
    """
    pass

class ProcessedDocument(BaseModel):
    """
    Модель для результата обработки.
    Содержит исходные и нормализованные данные.
    """
    original: Dict[str, Any]
    normalized: Dict[str, Any]