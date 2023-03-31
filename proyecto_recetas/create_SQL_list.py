import os
import sqlite3

def create_dishes_list():
    # Get the path of the directory containing the Python code file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # Create the database file in the same directory as the Python code file
    db_path = os.path.join(dir_path, 'dishes.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE dishes
             (id INTEGER PRIMARY KEY, name TEXT, ingredient_name TEXT, ingredient_quantity INTEGER)''')
    conn.commit()
    conn.close()


def create_ingredient_list():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(dir_path, 'ingredients.db')
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE ingredients
             (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')
    conn.commit()
    conn.close()

def select_create_list():
    asdf = int(input("Select what list do you want to create \n1) List of ingredients\n2) List of dishes\n"))
    if asdf == 1:
        create_ingredient_list()
        exit
    if asdf == 2:
        create_dishes_list()
        exit
