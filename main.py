from time import sleep
from db import *
import os
from prettytable import from_db_cursor

dottedLine = "\n\n-----------------------------------------------\n\n"

def clear():
    os.system('cls' if os.name == 'nt' else "printf '\033c'")

def welcome():
    clear()
    print('Welkom bij de suggestiesysteem!')
    sleep(1)
    name = input('Wat is je naam? ')
    sleep(1)
    print(f"Welkom {name}!")
    sleep(1)
    print("Hieronder volgt een paar selecties waaruit je kan kiezen!")
    sleep(3)
    menu()

def bekijkSpellen():
    clear()
    print("Hieronder worden alle spellen getoont die in de database voorkomen")
    sleep(1)
    c.execute("SELECT naam FROM games")
    mytable = from_db_cursor(c)
    print(mytable)
    sleep(1)
    print('Indien je terug wilt gaan naar het menu, type je « terug »')
    while True:
        back = input(">>> ")
        if back == 'terug':
            menu()
        else:
            print('Invalide invoer, probeer het opnieuw.')
def suggestieSysteem():
    clear()
    genreDict = {
        1: "Battle Royale",
        2: "FPS",
        3: "Casual",
        4: "Sports",
        5: "Horror",
        6: "MMORPG",
        7: "MMO",
        8: "Adventure",
        9: "RTS"
    }
    print("Welkom bij het suggestie systeem, laat ik je een paar genres tonen :)\n")
    sleep(2)
    for k, v in genreDict.items():
        print(f"[{k}] {v}", flush=True)
        sleep(.5)
    x = 1
    data = []
    print('\nWelke van de bovenstaande genres is het meest aantrekkelijk voor jou? Kies er 5 of minder, en gebruik de nummer toetsen om je keuze te maken')
    while x != 6:
        choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        choice = input(f"Keuze {x}. ")
        if choice in choices:
            data.append(int(choice))
            x += 1
        else:
            print('Invalid input! Kies de genres door middel van de nummer toetsen op je keyboard')
    clear()
    sleep(1)
    print('Interessante keuzes! Hieronder zie je de favoriete genres waar je op gekozen hebt\n')
    for key, value in genreDict.items():
        if key in data:
            print(f"[{key}] {value}", flush=True)
            sleep(.5)
    sleep(1)
    print('\nUit deze genres, die je hebt gekozen, welke genre trekt je het meest aan? Kies de genres door middel van de nummer toetsen op je keyboard')
    y = 1
    data2 = []
    while y != 2:
        choices = list(data)
        choice = int(input(">>> "))
        if choice in choices:
            data2.append(int(choice))
            y += 1
        else:
            print('Invalid input! Kies de genres door middel van de nummer toetsen op je keyboard')
    clear()
    sleep(1)
    print('Interessante keuzes! Hieronder zie je de genre die je hebt geselecteerd\n')
    favGenre = []
    for key, value in genreDict.items():
        if key in data2:
            print(f"[{key}] {value}")
            favGenre.append(value)
    sleep(1)
    print("\nSelecteer nu wat je wilt gaan doen\n")
    sleep(1)
    print("[1]  Games tonen die bij mij passen")
    sleep(1)
    print("[2]  Terug gaan naar het hoofdmenu")
    sleep(1)
    while True:
        choice = input(">>> ")
        if choice == '1':
            clear()
            print("Hieronder zul je de games zien die bij jou het best passen!\n")
            c.execute("SELECT * FROM games WHERE genre = ?", favGenre)
            mytable = from_db_cursor(c)
            print(mytable)
            sleep(1)
            print("\nBedankt voor het gebruiken van de suggestiesysteem! type « terug » als je terug wilt gaan naar het hoofdmenu")
            back = input(">>> ")
            while True:
                if back == "terug":
                    menu()
                else:
                    print("Invaliede input")    
        if choice == '2':
            clear()
            menu()

def menu():
    clear()
    print(dottedLine)
    print('[1]  Bekijk alle spellen')
    print('[2]  Krijg een spel gesuggereerd')
    print('[3]  Exit de applicatie')
    print(dottedLine)
    while True:
        option = input("Wat voor keuze word het? ")
        if option == '1':
            bekijkSpellen()
        if option == '2':
            suggestieSysteem()
        if option == '3':
            exit()

if __name__ == "__main__":
    welcome()
