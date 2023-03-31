import os
import sqlite3

def ingredient_connection():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(dir_path, 'ingredients.db')
    conn = sqlite3.connect(db_path)
    i = conn.cursor()
    return i
    
def modify_ingredients():
    i = ingredient_connection()
    i.execute("SELECT name, quantity FROM ingredients")
    rows = i.fetchall()
    print("Current ingredient quantities. Represent grams, litres and units accordingly.:")
    for row in rows:
        ingredient = row[0]
        quantity = row[1]
        print("{} - {}".format(ingredient, quantity))
    print("\nEnter the new quantities for each ingredient.\nPlease remember that units, weigth and capacity are not specified. Use grams and litres:")
    for row in rows:
        ingredient = row[0]
        current_quantity = row[1]
        new_quantity = int(input("{} - current quantity: {}. Enter new quantity: ".format(ingredient, current_quantity)))
        i.execute("UPDATE ingredients SET quantity = ? WHERE name = ?", (new_quantity, ingredient))
    i.connection.commit()
    i.connection.close()
    print("Quantities updated.")

def modify_single_ingredient():
    i = ingredient_connection()
    name = input("Enter the name of the ingredient to be modified: ")
    i.execute("SELECT name, quantity FROM ingredients WHERE name = ?", (name,))
    rows = i.fetchall()
    if len(rows) == 0:
        print("Ingredient not found.")
        return
    ingredient = rows[0][0]
    quantity = rows[0][1]
    new_quantity = int(input("{} - current quantity: {}. Enter new quantity: ".format(name, quantity)))
    i.execute("UPDATE ingredients SET quantity = ? WHERE name = ?", (new_quantity, ingredient))
    i.connection.commit()
    print("Quantities updated.")
    i.connection.close()
    
def printing_ingredients():
    i = ingredient_connection()
    i.execute("SELECT name, quantity FROM ingredients")
    rows = i.fetchall()
    print("The list of ingredients and their quantities: ")
    for row in rows:
        ingredient = row[0]
        quantity = row[1]
        print("{} - {}".format(ingredient, quantity))
        i.connection.close()

def add_new_ingredient():
    i = ingredient_connection()
    name = input("Enter the name of the new ingredient: ")
    quantity = input("Enter its quantity: ")
    i.execute("INSERT INTO ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
    i.connection.commit()
    i.connection.close()
    print("Ingredient added successfully.")


def clear_stock():
    i = ingredient_connection()
    i.execute("UPDATE ingredients SET quantity = 0")
    i.connection.commit()
    i.connection.close()
    print("All ingredient quantities set to zero.")


def remove_ingredient():
    i = ingredient_connection()
    name = input("Enter the name of the ingredient to be removed: ")
    i.execute("SELECT name FROM ingredients WHERE name = ?", (name,))
    row = i.fetchone()
    if row is None:
        print("Ingredient not found.")
    else:
        confirm = input("Are you sure you want to remove {} from the list? (Y/N)".format(name))
        if confirm.lower() == "y":
            i.execute("DELETE FROM ingredients WHERE name = ?", (name,))
            i.connection.commit()
            print("Ingredient removed successfully.")
        else:
            print("No changes were made.")
    i.connection.close()





