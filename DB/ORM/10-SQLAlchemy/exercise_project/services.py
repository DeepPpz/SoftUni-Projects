from models import Recipe, Chef
from main import Session


def create_recipe(name: str, ingredients: str, instructions: str):
    new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
    session.add(new_recipe)
    session.commit()


def update_recipe_by_name(name: str, new_name: str, new_ingredients: str, new_instructions: str):
    recipe_to_update = session.query(Recipe).filter_by(name=name).first()
    
    if recipe_to_update:
        recipe_to_update.name = new_name
        recipe_to_update.ingredients = new_ingredients
        recipe_to_update.instructions = new_instructions
        
        session.commit()


def delete_recipe_by_name(name: str):
    recipe_to_delete = session.query(Recipe).filter_by(name=name).first()
    
    if recipe_to_delete:
        session.delete(recipe_to_delete)
        session.commit()


def get_recipes_by_ingredient(ingredient_name: str):
    searched_recipes = session.query(Recipe).filter(Recipe.ingredients.ilike(f'%{ingredient_name}%')).all()

    return searched_recipes


def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str):
    try:
        session.begin()
        first_recipe = session.query(Recipe).filter_by(name=first_recipe_name).first()
        second_recipe = session.query(Recipe).filter_by(name=second_recipe_name).first()
        first_recipe.ingredients, second_recipe.ingredients = second_recipe.ingredients, first_recipe.ingredients
        session.commit()
        
    except Exception as e:
        session.rollback()
        print('An error occurred:', str(e))
    
    finally:
        session.close()


def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str):
    recipe = session.query(Recipe).filter_by(name=recipe_name).first()
    
    if recipe and recipe.chef:
        raise Exception(f'Recipe: {recipe.name} already has a related chef')
    
    chef = session.query(Chef).filter_by(name=chef_name).first()
    
    recipe.chef = chef
    session.commit()
    return f'Related recipe {recipe.name} with chef {chef.name}'


def get_recipes_with_chef():
    recipes_with_chef = session.query(Recipe.name, Chef.name.label('chef_name')).join(Chef, Recipe.chef).all()
    
    end_result = []
    for recipe, chef in recipes_with_chef:
        end_result.append(f'Recipe: {recipe} made by chef: {chef}')
    
    return '\n'.join(end_result)



### Tests ###
session = Session()

# Run the functions here



### Close the session ###
session.close()
