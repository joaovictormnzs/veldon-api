from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.task.controllers import task_controller
from app.task.schemas.task_schema import TaskCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tasks")
def criar_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_controller.criar_task(task, db)


@router.get("/tasks")
def listar_tasks(db: Session = Depends(get_db)):
    return task_controller.listar_tasks(db)


@router.get("/tasks/{task_id}")
def pegar_tarefa(task_id: int, db: Session = Depends(get_db)):
    return task_controller.pegar_tarefa(task_id, db)


@router.put("/tasks/{task_id}")
def atualizar_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return task_controller.atualizar_task(task_id, task, db)


@router.patch("/tasks/{task_id}/complete")
def concluida_task(task_id: int, db: Session = Depends(get_db)):
    return task_controller.concluir_task(task_id, db)


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return task_controller.deletar_task(task_id, db)