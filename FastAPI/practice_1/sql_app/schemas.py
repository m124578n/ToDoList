from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(BaseModel):
    pass


class Item(BaseModel):
    id: int
    owner_id: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    id: int
    is_active: bool
    items: List[Item] = []
    class Config:
        orm_mode = True
        