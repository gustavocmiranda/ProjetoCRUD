from fastapi import FastAPI
from databases.database import engine
from router import router
import models.product

models.product.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router=router)