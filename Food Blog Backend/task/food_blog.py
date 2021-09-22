import os
import sqlite3
import argparse
from sqlParser import sql_parser_for_arguments


# args = sys.argv
# db_name = args[1]
parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")

parser.add_argument("name")
parser.add_argument("-i", "--ingredients",
                    help="list of ingredients separated by commas.")
parser.add_argument("-m", "--meals",
                    help="list of meals separated by commas.")

args = parser.parse_args()
db_name = args.name


data = {"meals": ("breakfast", "brunch", "lunch", "supper"),
        "ingredients": (
            "milk", "cacao", "strawberry", "blueberry", "blackberry", "sugar"),
        "measures": ("ml", "g", "l", "cup", "tbsp", "tsp", "dsp", "")}


if os.path.isfile('food_blog.db'):
    pass
else:
    conn = sqlite3.connect(db_name)
    cursor_name = conn.cursor()
    cursor_name.execute('PRAGMA foreign_keys = ON;')
    cursor_name.execute(
        'CREATE TABLE meals(meal_id INTEGER PRIMARY KEY, meal_name VARCHAR('
        '60) NOT NULL UNIQUE);')
    cursor_name.execute('CREATE TABLE ingredients('
                        'ingredient_id INTEGER PRIMARY KEY,'
                        'ingredient_name VARCHAR(60) NOT NULL UNIQUE);')
    cursor_name.execute('CREATE TABLE measures('
                        'measure_id INTEGER PRIMARY KEY,'
                        'measure_name VARCHAR(60) UNIQUE);')
    cursor_name.execute('CREATE TABLE recipes('
                        'recipe_id INTEGER PRIMARY KEY,'
                        'recipe_name VARCHAR(60) NOT NULL,'
                        'recipe_description VARCHAR(60));')
    cursor_name.execute('CREATE TABLE serve('
                        'serve_id INTEGER PRIMARY KEY,'
                        'recipe_id INTEGER NOT NULL,'
                        'meal_id INTEGER NOT NULL,'
                        'FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id),'
                        'FOREIGN KEY(meal_id) REFERENCES meals(meal_id));')
    cursor_name.execute('CREATE TABLE quantity('
                        'quantity_id INTEGER PRIMARY KEY,'
                        'measure_id INTEGER NOT NULL,'
                        'ingredient_id INTEGER NOT NULL,'
                        'quantity INTEGER NOT NULL,'
                        'recipe_id INTEGER NOT NULL,'
                        'FOREIGN KEY(measure_id) REFERENCES measures(measure_id),'
                        'FOREIGN KEY(ingredient_id) REFERENCES ingredients(ingredient_id),'
                        'FOREIGN KEY(recipe_id) REFERENCES recipes(recipe_id));')
    cursor_name.execute('insert into meals (meal_id, meal_name) values '
                        '(1, "breakfast"),'
                        '(2, "brunch"),'
                        '(3, "lunch"),'
                        '(4, "supper");')
    cursor_name.execute('insert into ingredients (ingredient_id, ingredient_name) values '
                        '(1, "milk"), '
                        '(2, "cacao"),'
                        '(3, "strawberry"),'
                        '(4, "blueberry"),'
                        '(5, "blackberry"),'
                        '(6, "sugar");')
    cursor_name.execute('insert into measures (measure_id, measure_name) values '
                        '(1, "ml"),'
                        '(2, "g"),'
                        '(3, "l"),'
                        '(4, "cup"),'
                        '(5, "tbsp"),'
                        '(6, "tsp"),'
                        '(7, "dsp"),'
                        '(8, "");')
    conn.commit()


def add_recepie():
    conn = sqlite3.connect(db_name)
    cursor_name = conn.cursor()
    print("Pass the empty recipe name to exit.")
    is_recipe_name_not_empty = True
    # below while runs main logic needs to add other branch
    while True:
        rec_name = input("\nRecipe name: ")
        if len(rec_name) == 0:
            break

        rec_desc = input("Recipe description: ")
        id_last_row_recipe = cursor_name.execute('insert into recipes (recipe_name, '
                                                 'recipe_description) '
                                                 'values ('
                                                 '?, ?);',
                                                 (rec_name, rec_desc,)).lastrowid
        conn.commit()

        result = cursor_name.execute('select * from meals')
        all_rows = result.fetchall()
        for i in all_rows:
            for j in range(0, 2):
                print(i[j], end=' ')

        serving = input('\nWhen the dish can be served: ')
        serv_list = serving.split(' ')

        for meal in serv_list:
            cursor_name.execute('insert into serve (recipe_id, '
                                'meal_id) '
                                'values ('
                                '?, ?);', (id_last_row_recipe, meal,))
        conn.commit()

        while True:
            ingredients_info = input(
                "Input quantity of ingredient <press enter to stop>: ")
            if ingredients_info == '':
                break
            ingredients_info_list = ingredients_info.split(' ')

            if len(ingredients_info_list) > 2:
                quantity = ingredients_info_list[0]
                measure = ingredients_info_list[1]
                ingredient = ingredients_info_list[2]

                if measure not in data['measures']:
                    print("The measure is not conclusive! ")
                    continue
            else:
                quantity = ingredients_info_list[0]
                ingredient = ingredients_info_list[1]
                measure = ''

            if ingredient not in data['ingredients']:
                print("The ingredient is not conclusive! ")
                # continue
            mod_ingredient = ingredient + "%"
            res = cursor_name.execute('select * from measures where measure_name = ?;',
                                      (measure,))
            measure_id_prim_key = res.fetchall()
            # position in tuple

            res1 = cursor_name.execute('select * from ingredients '
                                       'where ingredient_name like ?;',
                                       (mod_ingredient,))
            ingredient_id_prim_key = res1.fetchall()
            # in tuple

            cursor_name.execute('insert into quantity (quantity, '
                                'measure_id,'
                                'ingredient_id,'
                                'recipe_id) '
                                'values('
                                '?, ?, ?, ?);', (quantity,
                                                 measure_id_prim_key[0][0],
                                                 ingredient_id_prim_key[0][0],
                                                 id_last_row_recipe,))

        conn.commit()
    conn.close()

def suggest_recipe(meals, ingredients):
    sql_phrase = sql_parser_for_arguments(meals, ingredients)
    conn = sqlite3.connect(db_name)
    cursor_name = conn.cursor()
    meals = cursor_name.execute(sql_phrase)
    recipes = meals.fetchall()
    # recipes_as_set = set()
    # for rec in recipes:
    #     recipes_as_set.add(rec[0])
    # szczepan = str(list(recipes_as_set))
    recipes_as_list = list()
    for rec in recipes:
        recipes_as_list.append(rec)
    if len(recipes_as_list) == 0:
        print('no such recipes')
    else:
        szczepan = str(recipes_as_list)
        print("Recipes selected for you: " + szczepan)




if (args.ingredients is None) and (args.meals is None):
    add_recepie()
else:
    suggest_recipe(args.meals, args.ingredients)

