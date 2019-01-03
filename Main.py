from Structure import Structure
from Player import Player
import os
import Code
import Addons


FILES = [
    '1.txt',
    '2.txt',
    '3.txt',
    'boss.txt',
    'weapon.txt'
    ]

for i in FILES:
    try:
        with open(i, encoding='utf-8') as f:
            if not f.readlines():
                input("Pusty plik " + i)
                exit(0)
    except FileNotFoundError:
        input("Brak pliku " + i)
        exit(0)

Addons.print_welcome()

sec = 0.05

while True:
    difficulty = None
    player = None
    player_class = None

    os.system('cls')
    Addons.menu(sec)
    sec = 0

    print("\nPodaj numer opcji")
    x = input(">>>")
    os.system('cls')

    if x == '1':
        while True:
            os.system('cls')
            print("=-"*18)
            print("Wybierz poziom trudności (1/2/3)\n0. Anuluj\n")
            print("1. Łatwy")
            print("2. Normalny")
            print("3. Trudny")
            difficulty = input("\n>>>")

            if difficulty in ["1", "2", "3"]:
                difficulty = int(difficulty)
                Code.score_multiplier = (difficulty / 3) + 1
                Code.generate(difficulty + 2)
                break

            elif difficulty == "0":
                difficulty = None
                break

        while difficulty is not None:
            os.system('cls')
            print("-="*18)
            print("Wybierz klasę (1/2/3)\n0. Anuluj\n")
            print("1. Wojownik")
            print("2. Mag")
            print("3. Łotrzyk")
            player_class = input("\n>>>")

            if player_class == "1":
                player = Player((4 - difficulty)*60)
                player.add_weapon("Noga", 11, 99, 5, "Kopnięcie przeciwnika")
                player.add_weapon("Miecz pazia", 40 - (difficulty - 1)*5, 70 - (difficulty - 1)*5, 5,
                                  "Cios mieczem pazia")
                player.add_armor("Zardzewiała zbroja", 15)
                break

            elif player_class == "2":
                player = Player((4 - difficulty)*40)
                player.add_weapon("Ręce", 11, 99, 5, "Proste zaklęcie rażące")
                player.add_weapon("Dębowa różdżka", 50 - (difficulty - 1)*5, 80 - (difficulty - 1)*5, 15,
                                  "Silne zaklęcie oszałamiające")
                player.add_armor("Stara szata", 5)
                break

            elif player_class == "3":
                player = Player((4 - difficulty)*50)
                player.add_weapon("Ręka", 11, 99, 5, "Sierpowy")
                player.add_weapon("Sztylet złodziejaszka", 40 - (difficulty - 1)*5, 75 - (difficulty - 1)*5, 10,
                                  "Cios sztyletem")
                player.add_armor("Skurzana tunika", 10)
                break

            elif player_class == "0":
                break

        if player is not None:
            structure = Structure(player, player_class + ".txt")
            player.load_weapons(int(player_class))
            Code.load_boss(player_class)

            while True:
                structure.p_move()
                if structure.end or player.dead:
                    break

    elif x == '2':
        Addons.score_table()

    elif x == '3':
        Addons.creators()

    elif x == '4':
        exit(0)
