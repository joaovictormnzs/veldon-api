from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///tasks.db")

Base = declarative_base()

session = sessionmaker(bind=db)

def pegar_db():
    db = session()
    try:
        yield db
    finally:
        db.close()