from sqlalchemy import Column, Integer, String, DateTime
import datetime
from src.database import Base

class ChatLog(Base):
    __tablename__ = "chat_logs"

    id = Column(Integer, primary_key=True, index=True)
    scholar_id = Column(String, index=True)
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
  
