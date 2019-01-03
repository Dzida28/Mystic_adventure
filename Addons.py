import time
import os
import pickle


def print_gameover():
    slow_print("""x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
x    _____          __  __ ______     ______      ________ _____    x
x   / ____|   /\   |  \/  |  ____|   / __ \ \    / /  ____|  __ \   x
x  | |  __   /  \  | \  / | |__     | |  | \ \  / /| |__  | |__) |  x
x  | | |_ | / /\ \ | |\/| |  __|    | |  | |\ \/ / |  __| |  _  /   x
x  | |__| |/ ____ \| |  | | |____   | |__| | \  /  | |____| | \ \   x
x   \_____/_/    \_\_|  |_|______|   \____/   \/   |______|_|  \_\  x
x                                                                   x
x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x""", 0.001)


def print_congrats():
    slow_print("""x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x
x   ___ ___  _  _  ___ ___    _ _____ _   _ _      _ _____ ___ ___  _  _ ___  x
x  / __/ _ \| \| |/ __| _ \  / \_   _| | | | |    / \_   _|_ _/ _ \| \| / __| x
x | (_| (_) | .` | (_ |   / / _ \| | | |_| | |__ / _ \| |  | | (_) | .` \__ \ x
x  \___\___/|_|\_|\___|_|_\/_/ \_\_|  \___/|____/_/ \_\_| |___\___/|_|\_|___/ x
x                                                                             x
x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x x""", 0.001)


def print_welcome():
    slow_print("""
 __          ________ _      _____ ____  __  __ ______ 
 \ \        / /  ____| |    / ____/ __ \|  \/  |  ____|
  \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__   
   \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|  
    \  /\  /  | |____| |___| |___| |__| | |  | | |____ 
     \/  \/   |______|______\_____\____/|_|  |_|______|
                      _______ ____  
                     |__   __/ __ \ 
                        | | | |  | |
                        | | | |  | |
                        | | | |__| |
                        |_|  \____/  """, 0.001)
    time.sleep(1)
    os.system('cls')
    slow_print(""" 
              __  ____     _______ _______ _____ _____ 
             |  \/  \ \   / / ____|__   __|_   _/ ____|
             | \  / |\ \_/ / (___    | |    | || |     
             | |\/| | \   / \___ \   | |    | || |     
             | |  | |  | |  ____) |  | |   _| || |____ 
             |_|  |_|  |_| |_____/   |_|  |_____\_____|
           _______      ________ _   _ _______ _    _ _____  ______ 
     /\   |  __ \ \    / /  ____| \ | |__   __| |  | |  __ \|  ____|
    /  \  | |  | \ \  / /| |__  |  \| |  | |  | |  | | |__) | |__   
   / /\ \ | |  | |\ \/ / |  __| | . ` |  | |  | |  | |  _  /|  __|  
  / ____ \| |__| | \  /  | |____| |\  |  | |  | |__| | | \ \| |____ 
 /_/    \_\_____/   \/   |______|_| \_|  |_|   \____/|_|  \_\______|


    """, 0.001)
    time.sleep(1)
    os.system('cls')


def creators():
    slow_print("""Twórcy:
    Wojciech Zamarski
    Nikodem Oleniacz
    Władysław Sokołowski
    Hieronim Dzieślewski""", 0.05)
    input("\nWciśnij ENTER, aby kontunuować...")


def menu(sec):
    print("=-="*7)
    slow_print("""        MENU
1. START
2. TABELA WYNIKÓW
3. TWÓRCY
4. WYJDŹ""", sec)


def score_table():
    if not os.path.isfile("scores.dat"):
        with open("scores.dat", "wb") as file:
            pickle.dump([0, 0, 0], file)

    while True:
        with open("scores.dat", "rb") as file:
            all_scores = pickle.load(file)

        all_scores.sort(reverse=True)

        print("Tabela wyników:")
        for i in range(0, 3):
            slow_print(str(i + 1) + ". " + str(all_scores[i]) + "\n", 0.03, newline=False)

        print("\nWciśnij ENTER, aby kontunuować...")
        p = input("...lub wpisz \"reset\" i wciśnij ENTER, aby zresetować tabelę wyników\n")

        if p.upper().startswith("RESET"):
            with open("scores.dat", "wb") as file:
                pickle.dump([0, 0, 0], file)
            os.system('cls')
        else:
            break


def countdown():
    print("\n")
    for i in range(3):
        slow_print(str(3 - i) + "...\n", 0.6, newline=False)


def slow_print(string, sec, newline=True):
    for i in range(0, len(string) - 2, 3):
        print(string[i:i + 3], end="", flush=True)
        time.sleep(sec)

    if len(string) % 3 == 1:
        print(string[len(string)-1], end="", flush=True)
    elif len(string) % 3 == 2:
        print(string[len(string)-2], end="", flush=True)
        print(string[len(string)-1], end="", flush=True)

    if newline:
        print("\n")
