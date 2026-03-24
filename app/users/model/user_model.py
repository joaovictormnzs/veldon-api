from sqlalchemy import Column, Integer, String
from app.database import Base 
from app.users.enums.user_Roler import User_Roler

class User(Base):

    __tablename__="users" 

    id = Column(int, primary_key= True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)