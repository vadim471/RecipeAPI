from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

recipe_categories = Table(
    "recipe_categories", Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipe.id")),
    Column("cat_id", Integer, ForeignKey("category.id"))
)

recipe_ingredients = Table(
    "recipe_ingredients", Base.metadata,
    Column("recipe_id", Integer, ForeignKey("recipe.id")),
    Column("ingr_id", Integer, ForeignKey("ingredient.id"))
)

class Recipe(Base):
    __tablename__ = "recipe"
    id = Column(Integer, primary_key = True, index = True)
    name_dish = Column(String, index = True)
    cook_time = Column(String)
    manual = Column(String)
    category = relationship("Category", secondary = recipe_categories, back_populates = "recipe")
    ingredient = relationship("Ingredient", secondary = recipe_ingredients, back_populates = "recipe")
    link = relationship("Link", back_populates = "recipe")

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key = True, index = True)
    name_cat = Column(String, unique = True)
    recipe = relationship("Recipe", secondary = recipe_categories, back_populates = "category")

class Ingredient(Base):
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key = True, index = True)
    name_ingr = Column(String, unique = True)
    recipe = relationship("Recipe", secondary = recipe_ingredients, back_populates = "ingredient")

class Link(Base):
    __tablename__ = "link_new"
    id = Column(Integer, ForeignKey("recipe.id"), primary_key = True)
    photo = Column(String)

    recipe = relationship("Recipe", back_populates = "link")