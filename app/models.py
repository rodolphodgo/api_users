import uuid
from sqlalchemy import Column, String, Enum, DateTime, func
from sqlalchemy.types import TypeDecorator, CHAR
from .database import Base
import enum

class Role(str, enum.Enum):
    user = "user"
    admin = "admin"

class GUID(TypeDecorator):
    impl = CHAR(32)
    cache_ok = True

    def process_bind_param(self, value, dialect):
        if value is not None:
            return value.hex
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return uuid.UUID(value)
        return value

class User(Base):
    __tablename__ = "users"
    
    id = Column(GUID(), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(Enum(Role), default=Role.user)
    created_at = Column(DateTime)