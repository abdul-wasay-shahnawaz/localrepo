from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator('name')
    @classmethod
    def name_check(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v.strip()

    @field_validator('password')
    @classmethod
    def password_check(cls, v):
        if len(v) < 4:
            raise ValueError('Password too short')
        return v


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True