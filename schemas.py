from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Пайдаланушы валидациясы 
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr  # Email форматын автоматты тексереді
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    username: str
    password: str

# Тауар валидациясы 
class ProductCreate(BaseModel):
    name: str = Field(..., min_length=2)
    category: str
    price: float = Field(..., gt=0)  # Бағасы 0-ден үлкен болуы тиіс
    description: Optional[str] = None

class ProductResponse(ProductCreate):
    id: int
    class Config:
        from_attributes = True

# Тапсырыс валидациясы 
class OrderCreate(BaseModel):
    product_id: int
    quantity: int = Field(1, ge=1)
