from pydantic import BaseModel
from typing import List, Optional


class IngredientBase(BaseModel):
    name_ingr: str

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name_cat: str

    class Config:
        from_attributes = True

class LinkBase(BaseModel):
    photo: str

    class Config:
        from_attributes = True

class RecipeBase(BaseModel):
    name_dish: str
    cook_time: str
    manual: str



class RecipeSchema(RecipeBase):
    id: int
    ingredient: List[IngredientBase] = []
    category: List[CategoryBase] = []
    link: List[LinkBase] = None

    class Config:
        from_attributes = True

