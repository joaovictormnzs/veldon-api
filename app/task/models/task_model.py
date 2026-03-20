from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from app.database import Base

class Task(Base):

        __tablename__ = "tasks"

        id = Column(Integer, primary_key=True, index=True)
        tittle = Column(String)
        description = Column(String)
        priority = Column(String)
        completed = Column(Boolean, default=False)
        created_by = Column(DateTime, default=datetime.utcnow)