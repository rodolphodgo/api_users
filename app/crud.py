from sqlalchemy.orm import Session
from .models import User, Role
from .schemas import UserCreate, UserUpdate
from uuid import UUID
import pendulum

def get_all_user(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: UUID):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name, 
        email=user.email,
        role=user.role,
        created_at=pendulum.now("America/Sao_Paulo")
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: UUID, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if user.name is not None:
            db_user.name = user.name
        if user.email is not None:
            db_user.email = user.email
        if user.role is not None:
            db_user.role = user.role

        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def delete_user(db: Session, user_id: UUID):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()