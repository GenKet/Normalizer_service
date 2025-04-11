from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.services import document_service
from app.schemas.document_models import DocumentInput, ProcessedDocument
from app.utils.body_parser import parse_request
import logging

router = APIRouter()

@router.post("/process", response_model=ProcessedDocument)
async def process_document_endpoint(request: Request, db: Session = Depends(get_db)):
    """
    Эндпоинт для обработки юридических документов в форматах JSON и XML.
    Ответ всегда возвращается в формате JSON (согласно модели ProcessedDocument),
    а результат обработки сохраняется в базе данных.
    """   
    data_dict = await parse_request(request)
    if not data_dict:
        raise HTTPException(status_code=400, detail="Неверный формат данных")
    try:
        document_input = DocumentInput.model_validate(data_dict)  
        return document_service.process_documents(document_input.root, db)
    except Exception as e:
        logging.exception("Ошибка обработки документа")
        raise HTTPException(status_code=500, detail=str(e))