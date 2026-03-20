from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TaskCreate(BaseModel):
    tittle : str
    description: Optional[str]
    priority: str

class TaskResponde(BaseModel):
    id: int
    tittle: str
    description: Optional[str]
    priority: str
    conmpleted: bool
    created_by: datetime

    class Config:
        orm_mode = True