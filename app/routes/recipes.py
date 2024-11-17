from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import get_recipes, get_recipes_by_category, get_recipes_by_ingredients
from app.schemas import RecipeSchema
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()

@router.get("/recipes", response_model = List[RecipeSchema])
def list_recipes(exclude: List[str] = None, db: Session = Depends(get_db)):
    recipes = get_recipes(db, exclude)
    return recipes

@router.get("/recipes/category", response_model = List[RecipeSchema])
def recipes_by_category(category: str, exclude: List[str] = None, db: Session = Depends(get_db)):
    recipes = get_recipes_by_category(db, category, exclude)
    return recipes

@router.get("/recipes/ingredients", response_model = List[RecipeSchema])
def recipes_by_ingeridents(ingredients: List[str], exclude: List[str] = None, db: Session = Depends(get_db)):
    recipes = get_recipes_by_ingredients(db, ingredients, exclude)
    return recipes