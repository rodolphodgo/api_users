from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import engine, get_db
from typing import List
from uuid import UUID

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/users/", response_model=List[schemas.UserResponse])
def read_all_users(db: Session = Depends(get_db)):
    """Retorna todos os usuários cadastrados"""
    users = crud.get_all_user(db)
    return users

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    """Retorna o usuário de acordo com o ID informado"""
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return db_user

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Insere um novo usuário ao banco de dados"""
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.create_user(db=db, user=user)

@app.delete("/users/{user_id}")
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    """Deleta o usuário de acordo com o ID informado"""
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    crud.delete_user(db=db, user_id=user_id)
    return {"message": "Usuário deletado com sucesso"}

@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: UUID, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    """Atualiza o usuário de acordo com o ID informado"""
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    updated_user = crud.update_user(db, user_id, user)
    return updated_user