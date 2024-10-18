# REPRESENTACAO DAS INTERACOES COM O USUARIO
from pydantic import BaseModel, PositiveFloat, EmailStr, field_validator
from enum import Enum
from datetime import datetime
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    email_fornecedor: EmailStr

class ProductCreate(ProductBase):
    #created_at: datetime
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_atributes = True

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None