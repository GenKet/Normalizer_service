from sqlalchemy import Column, Integer, JSON, DateTime, func
from app.db.db import Base

class ProcessedDocumentDB(Base):
    __tablename__ = "processed_documents"

    id = Column(Integer, primary_key=True, index=True)
    original_data = Column(JSON, nullable=False)
    normalized_data = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
