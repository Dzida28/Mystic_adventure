# -*- coding: utf-8 -*-
import random as r
import os
import Addons

code = ""
unknown = []
boss_name = ""
boss_pict = ""
score_multiplier = 1


def generate(amount):
    global code
    global unknown

    code = "".join(map(lambda a: str(r.randint(1, 9)), range(amount)))
    unknown = list(map(lambda a: str("*"*a + code[a] + "*"*(amount-a-1)), range(amount)))


def get_code_digit():
    global unknown
    if len(unknown) > 0:
        num = r.choice(unknown)
        unknown.remove(num)
        return "\"Kod: " + num + "\"\n"
    else:
        return "Kod: " + code


def return_known_code():
    known = list(code)

    for i in unknown:
        for x in range(len(i)):
            if i[x] != "*":
                known[x] = "*"
                break
    known = "".join(known)
    return known


def game_end(player):
    sec = 0.005
    Addons.countdown()
    Addons.slow_print("\nWylądowałeś w pokoju przeznaczenia!", 0.05)
    input("\nWciśnij ENTER, aby kontunuować...")

    while True:
        os.system('cls')
        print("-"*20)
        Addons.slow_print("""Jesteś w pokoju przeznaczenia\n
Twoje serce zaczyna bić szybciej. Przed Tobą znajdują się duże straszliwe wrota.
Wygląda na to że, aby je otworzyć należy podać odpowiedni kod.""", sec, newline=False)
        if return_known_code() == code:
            print("\nZnasz już cały kod: " + code)
        else:
            print("\nZnasz część cyfr kodu: " + return_known_code())

        Addons.slow_print("""Jednak czy jesteś na tyle odważny aby przekonać się co kryje się za tymi drzwiami?
Widzisz, że masz też prawdopodobną możliwość powrotu przez ten sam portal,
z którego tu przyszedłeś.""", sec)
        sec = 0
        print("Co robisz? (1/2)\n")
        print("1. Próbujesz wpisać kod")
        print("2. Wchodzisz do portalu\n")
        p = input(">>>")

        if p == "1":
            if guess(player) or player.dead:
                return True

        elif p == "2":
            Addons.countdown()
            Addons.slow_print("Portal przenosi Cię z powrotem do pokoju startowego.\n", 0.05)
            input("\nWciśnij ENTER, aby kontunuować...")
            return False


def guess(player):
    print("\nPodaj kod")
    code_input = input(">>>")

    if code == code_input:
        Addons.slow_print("\nPodałeś właściwy Kod!\n", 0.05, newline=False)
        player.update_lvl(50)
        Addons.slow_print("Wrota otwierają się z wielkim piskiem...\n" + boss_name + " chce pożreć Twoją duszę!", 0.1)
        Addons.slow_print(boss_pict, 0.0001)
        input("\nWciśnij ENTER, aby kontunuować...")

        player.fight(boss_name, int(score_multiplier*player.max_hp/9)*10)
        if not player.dead:
            Addons.slow_print("Teraz już nic nie stoi na przeszkodzie, aby opuścić to miejsce.\nOdzyskałeś wolność...",
                              0.05)
            Addons.print_congrats()
            print("\nKONIEC GRY")
            player.save_score(score_multiplier)
            input("\nWciśnij ENTER, aby kontunuować...")
        os.system('cls')
        return True

    else:
        Addons.slow_print("\nZły kod.\nZ podłogi wysuwają się kłujące kolce.\n", 0.05, newline=False)
        player.update_hp(10)
        if not player.dead:
            input("\nWciśnij ENTER, aby kontunuować...")
    return False


def load_boss(player_class):
    global boss_name
    global boss_pict

    boss_name = ['Deathwing', 'Czarnoksieznik', 'Ksiezniczka'][int(player_class) - 1]
    boss_pict = ""

    with open("boss.txt", "r") as f:
        tmp = 0
        for line in f:
            if line.startswith("x x"):
                tmp += 1
            if tmp > int(player_class)*2:
                break
            if tmp > int(player_class)*2 - 2:
                boss_pict += line
