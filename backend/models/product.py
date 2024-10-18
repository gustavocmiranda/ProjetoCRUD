# regra de negocio
# IGUAL AO BANCO DE DADOS
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from databases.database import Base

class ProductModel(Base):
    __tablename__ = 'products' # nome da tabela
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
    email_fornecedor = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())