import os
import sqlite3
from modify_ingredients import *
from modify_dishes import *
from create_SQL_list import *
from functionalities import *

def makeable_dishes():
    dir_path = os.path.dirname(os.path.realpath(__file__))

    i = ingredient_connection()
    d = dish_connection()

    i.execute("SELECT name, quantity FROM ingredients")
    ingredients_list = dict(i.fetchall())
    d.execute("SELECT name, ingredient_name, ingredient_quantity FROM dishes")
    dishes_list = d.fetchall()

    possible_dishes = set()
    for dish in dishes_list:
        dish_name, ingredient_name, required_quantity = dish
        if ingredient_name in ingredients_list:
            if required_quantity <= ingredients_list[ingredient_name]:
                possible_dishes.add(dish_name)

    print("You can cook the following dishes with the available ingredients:")
    for dish in possible_dishes:
        print(dish)

    d.connection.close()
    i.connection.close()

print("Welcome! I am your food and menu management service (F.M.M.S.)!")
opening_sound()

def initialize():
    while True:
        choice = int(input("Are you a new user? \n1) Yes, I am a new user/I want to erase all information\n2) I am not a new user\n"))
        if choice == 1:
            while True:
                ensure = int(input("Are you sure that you are a new user? \nIf you proceed all the previous information will be deleted. \n1) Proceed to erase and star anew \n2) Keep my information and access the main menu\n" ))
                if ensure == 1:
                    print("\n\nI am pleased to guide you throughout the first steps and set-up of your own F.M.M.S. \n\nYou will need to provide information about the food that you have at home in order for me to offer you a proper service. \nNow you will be presented with a blank list of basic ingredients, and you need to tell me hom many of those ingredients you have. \nTo make the things easier to understand, when we speak about a quantity of an ingredient we will set grams for bulk ingredients, units for things easily enumerable and milliliters for liquids. Don't worry about it, for recipees we will use easier units.")
                    db_file_path = "proyecto_recetas\ingredients.db"
                    os.remove(db_file_path)
                    create_ingredient_list()
                    db_file_path2 = "proyecto_recetas\dishes.db"
                    os.remove(db_file_path2)
                    create_dishes_list()
                    modify_ingredients()
                    print("Now you will be redirected to the main menu, where you can browse between different functionalities and services. \nI made sure that there are a few simple recipees for you to start playing around, but as an assistant I will need guidance and feedback to be as useful as I can.\n")
                    menu()
                if ensure == 2: 
                    menu()
                else:
                    print("Unvalid request.")
        if choice == 2:
            menu()
        else:
            print("Unvalid request.")

def menu ():
    while True:
        options = int(input("1) See and modify your ingredients\n2) to preview, read or create dishes\n3) Useful functionalities\n4) Recipees menu\n5) Close the F.M.M.S.\n"))
        if options == 1:
            ingredients()
        if options == 2:
            dishes()
        if options == 3:
            functionalities()
        if options == 4:
            recipees()
        if options == 5:
            print("I hope I been helpful! Have a nice day.")
            exit()
        else:
            print("Unvalid request.")

def ingredients():
    while True:
        ingredients_options = int(input("Select your option:\n\n1) Consult the ingredients that you have\n2) Add a new ingredient\n3) Modify the quantity of an ingredient\n4) Review and modify all your ingredients\n5) Remove an ingredient\n6) Clear your stock and set all the ingredients to null quantity.\n7) Access the dishes menu\n8) Access recipees menu\n9) Access other funcionalities\n10) Close the F.M.M.S.\n"))
        match ingredients_options:
            case 1:
                printing_ingredients()
            case 2:
                add_new_ingredient()
            case 3:
                modify_single_ingredient()
            case 4:
                modify_ingredients()
            case 5:
                remove_ingredient()
            case 6:
                clear_stock()
            case 7:
                dishes()
            case 8:
                recipees()
            case 9:
                functionalities()
            case 10:
                print("I hope I been helpful! Have a nice day.")
                exit()
            case _:
                print("\nWrong selection.\n")

def dishes():
    while True:
        dishes_options = int(input("Select your option:\n1) Create dish\n2) Delete dish\n3) Modify Dish\n4) See required ingredients for a dish\n5) Access the recipees menu\n6) Access the ingredients menu\n7) Access other funcitonalies\n8) Close the F.M.M.S.\n"))
        match dishes_options:
            case 1:
                create_dish()
            case 2:
                delete_dish()
            case 3:
                modify_dish()
            case 4:
                print_dish_ingredients()
            case 5:
                recipees()
            case 6:
                ingredients()
            case 7:
                functionalities()
            case 8:
                print("I hope I been helpful! Have a nice day.")
                exit()
            case _:
                print("\nWrong selection.\n")

def functionalities():
    while True:
        selection = int(input("\n1) Timer!\n2) Unit conversion!\n3) Back to ingredient's menu\n4) Back to dishe's menu\n5) Open the recipees menu\n6) Close the F.M.M.S.\n"))
        match selection:
            case 1:
                count_beep()
            case 2:
                conversion()
            case 3:
                ingredients()
            case 4:
                dishes()
            case 5:
                recipees()
            case 6:
                print("I hope I been helpful! Have a nice day.")
                exit()
            case _:
                print("\nWrong selection.\n")

def recipees():
    while True:
        things = int(input("1) Print a list of all the recipees\n2) Open a specific recipee by name\n3) Back to ingredient's menu\n4) Back to dishe's menu\n5) Access other funcionalities\n6) Close the F.M.M.S.\n"))
        match things:
            case 1:
                list_files()
            case 2:
                open_recipee()
            case 3:
                ingredients()
            case 4:
                dishes()
            case 5:
                functionalities()
            case 6:
                print("I hope I been helpful! Have a nice day.")
                exit()
            case _:
                print("\nWrong selection.\n")

initialize()
