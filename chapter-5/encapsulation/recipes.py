# recipes.py
#
# This module demonstrate the concept of encapsulation within a Python module.

def new(name, num_servings):
    """ Create and return a new recipe.
    """
    return {'name'         : name,
            'num_servings' : num_servings,
            'instructions' : [],
            'ingredients'  : []}


def add_instruction(recipe, instruction):
    """ Add an instruction to the recipe.
    """
    recipe['instructions'].append(instruction)


def add_ingredient(recipe, ingredient, amount, units):
    """ Add an ingredient to the recipe.
    """
    recipe['ingredients'].append({'ingredient' : ingredient,
                                  'amount'     : amount,
                                  'units'      : units})


def get_name(recipe):
    return recipe['name']


def get_num_servings(recipe):
    return recipe['num_servings']


def get_instructions(recipe):
    return recipe['instructions']


def get_ingredients(recipe):
    return recipe['ingredients']


def to_string(recipe, num_servings):
    """ Return a list of strings with a description of this recipe.

        The recipe will be customized for the given number of servings.
    """
    s = []
    s.append("Recipe for {}, {} servings:".format(recipe['name'],
                                                  num_servings))
    s.append("")
    s.append("Ingredients:")
    s.append("")
    for ingredient in recipe['ingredients']:
        s.append("    {} - {} {}".format(ingredient['ingredient'],
                                         ingredient['amount'] * num_servings /
                                         recipe['num_servings'],
                                         ingredient['units']))
    s.append("")
    s.append("Instructions:")
    s.append("")
    for i,instruction in enumerate(recipe['instructions']):
        s.append("{}. {}".format(i+1, instruction))

    return s

