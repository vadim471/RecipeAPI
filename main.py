from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routes import recipes


app = FastAPI()

app.include_router(recipes.router, prefix = "")


@app.get("/")
def read_root():
    return {"message": "Welcome"}
