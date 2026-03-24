from pydantic import BaseModel
from app.users.enums.user_Roler import UserRole

class UserCreate(BaseModel):
    name: str
    role: UserRole

class UserResponse(BaseModel):
    id: int
    name: str
    role: UserRole

    class Config:
        orm_mode = True