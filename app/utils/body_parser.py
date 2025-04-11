from fastapi import Request
from app.utils.xml_parser import xml_to_dict

async def parse_request(request: Request) -> dict: 
    """
    Парсинг тела запроса для различных форматов (JSON, XML).
    Возвращает словарь с данными документа.
    """
    content_type = request.headers.get("Content-Type", "")
    body = await request.body()
    if "application/json" in content_type:
        return await request.json()
    elif "application/xml" in content_type or "text/xml" in content_type:
        return xml_to_dict(body.decode("utf-8"))
    return None
