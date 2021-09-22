# The logic of the query should be (ingredient1 AND ingredient2 AND ...) AND (meal1 OR meal2 OR ...)
# (ingredient_name = 'sugar' OR ingredient_name ='milk')

def sql_parser_for_arguments(meals, ingredients):
    meals_amount = len(meals.split(','))
    ingredients_amount = len(ingredients.split(','))

    meals_query = ''
    if meals_amount == 1:
        meals_query = "meal_name = '" + meals + "'"
    if meals_amount == 2:
        meals_query = "meal_name = '" + meals.split(',')[
            0] + "' OR meal_name =  '" + \
                      meals.split(',')[1] + "'"


    ingredients_query = ''
    ingredients_query_second_half = ''
    if ingredients_amount == 1:
        ingredients_query = "ingredient_name = '" + ingredients + "'"
        ingredients_query_second_half = "ingredient_name = '" + ingredients + "'"
    if ingredients_amount == 2:
        ingredients_query = "ingredient_name = '" + ingredients.split(',')[
            0] + "'"
        ingredients_query_second_half = "ingredient_name = '" + ingredients.split(',')[
            1] + "'"



    # phrase = "SELECT recipe_name from recipes where recipe_id in (SELECT recipe_id from quantity where ingredient_id IN (SELECT ingredient_id from ingredients where (" + ingredients_query + "))) AND recipe_id in (SELECT recipe_id from serve where meal_id IN (SELECT meal_id from meals where(" + meals_query + ")));"


    phrase ="SELECT recipe_name from recipes where recipe_id in (SELECT DISTINCT recipe_id from quantity AS recipes Where ingredient_id in (SELECT ingredient_id from ingredients AS my_ingred where (" + ingredients_query + ")) AND exists ( SELECT recipe_id from quantity WHERE ingredient_id in (SELECT ingredient_id from ingredients where ( " + ingredients_query_second_half + ")) AND recipe_id = recipes.recipe_id)) AND recipe_id in (SELECT recipe_id from serve where meal_id IN (SELECT meal_id from meals where(" + meals_query + ")));"
    return phrase
    #
    #
