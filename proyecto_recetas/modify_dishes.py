import os
import sqlite3

def dish_connection():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    db_path = os.path.join(dir_path, 'dishes.db')
    conn = sqlite3.connect(db_path)
    d = conn.cursor()
    return d

def create_dish():
    d = dish_connection()
    name = input("Enter the name of the dish: ")
    d.execute("INSERT INTO dishes (name) VALUES (?)", (name,))
    d.connection.commit()
    dish_id = d.lastrowid +1
    while True:
        ingredient_name = input("Enter a required ingredient name or type 'done' to finish this stage and write the recipee in a new .txt file: ")
        if ingredient_name == 'done':
            file_path = os.path.join(os.getcwd(), name + ".txt")
            with open(file_path, "w") as file:
                print(f"File '{name}.txt' created successfully.")
                file.write("Please, write here your " + name + " recipee!")
            os.startfile(file_path)
            break
        quantity = int(input("Enter the required quantity for {}: ".format(ingredient_name)))
        d.execute("INSERT INTO dishes (id, name, ingredient_name, ingredient_quantity) VALUES (?, ?, ?, ?)",
                  (dish_id, name, ingredient_name, quantity))
        dish_id += 1
        d.connection.commit()
    print("Dish {} added successfully".format(name))
    d.connection.close()

def delete_dish():
    d = dish_connection()
    name = input("Enter the name of the dish to be deleted: ")
    d.execute("DELETE FROM dishes WHERE name = ?", (name,))
    d.connection.commit()
    d.connection.close()
    print("Dish with name {} deleted successfully".format(name))
    filepath = os.path.join(os.getcwd(), name + ".txt")
    os.remove(filepath)

def modify_dish():
    d = dish_connection()
    name = input("Enter the name of the dish to be modified: ")
    d.execute("SELECT * FROM dishes WHERE name = ?", (name,))
    dish = d.fetchall()
    if not dish:
        print("No dish with name {} found".format(name))
    else:
        print("Previous ingredients:")
        for row in dish[1:]:
            print("- {} ({})".format(row[2], row[3]))
    d.execute("SELECT * FROM dishes WHERE name = ?", (name,))
    d.execute("DELETE FROM dishes WHERE name = ?", (name,))
    d.connection.commit()
    d.execute("INSERT INTO dishes (name) VALUES (?)", (name,))
    dish_id = d.lastrowid +1
    while True:
        ingredient_name = input("Enter an ingredient name or type 'done' to finish: ")
        if ingredient_name == 'done':
            break
        quantity = int(input("Enter the required quantity for {}: ".format(ingredient_name)))
        d.execute("INSERT INTO dishes (id, name, ingredient_name, ingredient_quantity) VALUES (?, ?, ?, ?)",
                  (dish_id, name, ingredient_name, quantity))
        dish_id += 1
        d.connection.commit()
    print("Dish with name {} modified successfully".format(name))
    d.connection.close()

def print_dish_ingredients():
    d = dish_connection()
    name = input("Enter the name of the dish to print: ")
    d.execute("SELECT * FROM dishes WHERE name = ?", (name,))
    dish = d.fetchall()
    if not dish:
        print("No dish with name {} found".format(name))
        d.connection.close()
    else:
        print("Ingredients:")
        for row in dish[1:]:
            print("- {} ({})".format(row[2], row[3]))
            d.connection.close()





