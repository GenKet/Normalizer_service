import uvicorn
from fastapi import FastAPI
from app.db.db import engine, Base
import app.db.models
from app.routers import document_router
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Legal Document Processor API",
    description="API для обработки юридических документов (JSON/XML) с нормализацией и объединением данных.",
    version="1.0.0"
)

app.include_router(document_router.router, prefix="/api", tags=["documents"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)