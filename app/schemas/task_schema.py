from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.enums.task_priority import TaskPriority

class TaskCreate(BaseModel):
    title : str
    description: Optional[str]
    priority: TaskPriority = TaskPriority.BAIXA
    created_by_id: int
    assigned_to_id: Optional[int] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    priority: TaskPriority = TaskPriority.BAIXA
    completed: bool
    created_by_id: int
    assigned_to_id: int

    class Config:
        from_attributes = True