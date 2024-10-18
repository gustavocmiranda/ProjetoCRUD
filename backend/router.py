from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from databases.database import SessionLocal, get_db
from backend.schemas.schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import(
    create_product,
    get_products,
    get_product,
    update_product,
    delete_product
)

router = APIRouter()


@router.get(path="/products/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

@router.get(path="/products/{product_id}", response_model=ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não existe.")
    return  db_product

@router.post(path="/products/", response_model=ProductResponse)
def post_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.delete(path="/products/{product_id}", response_model=ProductResponse)
def delete_prod(product_id: int, db: Session = Depends(get_db)):
    product_db = delete_product(db, product_id)

    if product_db is None:
        raise HTTPException(status_code=404, detail="Produto não existente.")

    return product_db

@router.put("/products/{product_id}", response_model=ProductResponse)
def atualizar_product(products_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    product_db = update_product(db, products_id, product)

    if product_db is None:
        raise HTTPException(status_code=404, detail="Produto não existente.")
    
    return product_db