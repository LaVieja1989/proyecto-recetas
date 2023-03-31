from winsound import Beep, PlaySound
from time import sleep
import os
import subprocess

def countdown():
    for i in range(int(float(input("Hello! I am your timer! Tell me how many minutes you want me to count! ")) * 120)):
        print(0.5 + (i / 2))
        sleep(0.5)

def beep():
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 500 ms == 0.5 secs
    Beep(frequency, duration)
    Beep(frequency, duration)

def count_beep():
    countdown()
    beep()
    beep()
    beep()
    print("End of countdown!")

def conversion():
    def litres_to_pints(litres):
        pints = litres * 2.11338
        return pints

    def pints_to_litres(pints):
        litres = pints / 2.11338
        return litres

    def grams_to_pounds_ounces(grams):
        pounds = grams / 453.59237
        ounces = (pounds - int(pounds)) * 16
        pounds = int(pounds)
        return (pounds, ounces)

    def pounds_ounces_to_grams(pounds, ounces):
        grams = (pounds * 453.59237) + (ounces * 28.34952 / 16)
        return grams

    unit_type = input("What unit type would you like to convert? (litres/pints/grams/pounds/ounces): ")
    value = float(input("Enter the value to convert: "))

    if unit_type == "litres":
        pints = litres_to_pints(value)
        print(f"{value} litres = {pints:.2f} pints")
    elif unit_type == "pints":
        litres = pints_to_litres(value)
        print(f"{value} pints = {litres:.2f} litres")
    elif unit_type == "grams":
        pounds, ounces = grams_to_pounds_ounces(value)
        print(f"{value} grams = {pounds} pounds {ounces:.2f} ounces")
    elif unit_type == "pounds":
        grams = pounds_ounces_to_grams(value, 0)
        print(f"{value} pounds = {grams:.2f} grams")
    elif unit_type == "ounces":
        pounds, ounces = grams_to_pounds_ounces(value * 28.34952)
        print(f"{value} ounces = {pounds} pounds {ounces:.2f} ounces")
    else:
        print("Invalid unit type. Please enter litres, pints, grams, pounds, or ounces.")

def open_recipee():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = input("Enter file name: ") + ".txt"

    try:
        file_path = os.path.join(dir_path, file_name)
        print(f"Opening file '{file_name}' in notepad...")
        subprocess.Popen(['notepad.exe', file_path])
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

def list_files():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_list = [f[:-4] for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and f.endswith('.txt')]
    if len(file_list) == 0:
        print("No text files found in this directory.")
    else:
        print("Text files in this directory:")
        for file_name in file_list:
            print(file_name)

def opening_sound():
    PlaySound("pan_opening.wav", 0)


