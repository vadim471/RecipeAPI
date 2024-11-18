from sqlalchemy.orm import Session, joinedload
from .models import Recipe, Category, Ingredient, recipe_categories, recipe_ingredients
from .schemas import RecipeSchema
def get_recipes(session: Session, exclude: list[str] = None):
    query = session.query(Recipe)
    if exclude:
        query = query.filter(~Recipe.ingredient.any(Ingredient.name_ingr.in_(exclude)))
    recipes = query.options(
        joinedload(Recipe.ingredient),
        joinedload(Recipe.link),
        joinedload(Recipe.category)
        ).limit(10).all()
    return [RecipeSchema.model_validate(recipe) for recipe in recipes]

def get_recipes_by_category(session: Session, category_name: str, exclude: list[str] = None):
    query = (
        session.query(Recipe)
        .join(recipe_categories, recipe_categories.c.recipe_id == Recipe.id)
        .join(Category, recipe_categories.c.cat_id == Category.id)
        .filter(Category.name_cat == category_name)
    )
    if exclude:
        query = query.filter(~Recipe.ingredient.any(Ingredient.name_ingr.in_(exclude)))
    recipes = query.options(
        joinedload(Recipe.link),
        joinedload(Recipe.ingredient),
        joinedload(Recipe.category)
        ).limit(10).all()
    return [RecipeSchema.model_validate(recipe) for recipe in recipes]

def get_recipes_by_ingredients(session: Session, ingredients: list[str], exclude: list[str] = None):
    query = session.query(Recipe).join(Recipe.ingredient)
    for term in ingredients:
        query = query.filter(Ingredient.name_ingr.ilike(f"%{term}%"))
    if exclude:
        query = query.filter(~Recipe.ingredient.any(Ingredient.name_ingr.in_(exclude)))
    recipes = query.options(
        joinedload(Recipe.link),
        joinedload(Recipe.ingredient),
        joinedload(Recipe.category)
        ).limit(10).all()
    return [RecipeSchema.model_validate(recipe) for recipe in recipes]