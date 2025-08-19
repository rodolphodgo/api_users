from pydantic import BaseModel, EmailStr
from typing import Optional, List
from uuid import UUID
from .models import Role
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: str
    role: Optional[Role] = Role.user

class UserResponse(BaseModel):
    id: UUID
    name: str
    email: str
    role: Role
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[Role]