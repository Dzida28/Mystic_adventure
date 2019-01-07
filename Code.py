# -*- coding: utf-8 -*-
import random as r
import os
import Addons


class Code:
    def __init__(self):
        self.code = ""
        self.unknown = []
        self.boss_name = ""
        self.boss_pict = ""
        self.score_multiplier = 1

    def __str__(self):
        return self.code

    def generate(self, amount):
        self.code = "".join(map(lambda a: str(r.randint(1, 9)), range(amount)))
        self.unknown = list(map(lambda a: str("*" * a + self.code[a] + "*" * (amount - a - 1)), range(amount)))

    def get_code_digit(self):
        if self.unknown:
            num = r.choice(self.unknown)
            self.unknown.remove(num)
            return "\"Kod: %s\"\n" % num
        else:
            return "\"Kod: %s\"\n" % self

    def return_known_code(self):
        known = list(self.code)

        for i in self.unknown:
            index = list(map(lambda a: a != "*", list(i))).index(True)
            known.insert(index, "*")
            known.pop(index+1)

        known = "".join(known)
        return known

    def game_end(self, player):
        sec = 0.005
        Addons.countdown()
        Addons.slow_print("\nWylądowałeś w pokoju przeznaczenia!", 0.05)
        input("\nWciśnij ENTER, aby kontunuować...")

        while True:
            os.system('cls')
            print("-" * 20)
            Addons.slow_print("""Jesteś w pokoju przeznaczenia\n
Twoje serce zaczyna bić szybciej. Przed Tobą znajdują się duże straszliwe wrota.
Wygląda na to że, aby je otworzyć należy podać odpowiedni kod.""", sec, newline=False)
            if self.return_known_code() == self.code:
                print("\nZnasz już cały kod: " + self.code)
            else:
                print("\nZnasz część cyfr kodu: " + self.return_known_code())

            Addons.slow_print("""Jednak czy jesteś na tyle odważny aby przekonać się co kryje się za tymi drzwiami?
Widzisz, że masz też prawdopodobną możliwość powrotu przez ten sam portal,
z którego tu przyszedłeś.""", sec)
            sec = 0
            print("Co robisz? (1/2)\n")
            print("1. Próbujesz wpisać kod")
            print("2. Wchodzisz do portalu\n")
            p = input(">>>")

            if p == "1":
                if self.guess(player):
                    return True

            elif p == "2":
                Addons.countdown()
                Addons.slow_print("Portal przenosi Cię z powrotem do pokoju startowego.\n", 0.05)
                input("\nWciśnij ENTER, aby kontunuować...")
                return False

    def guess(self, player):
        print("\nPodaj kod")
        code_input = input(">>>")

        while len(code_input) != len(self.code):
            code_input = input("\n>>>")

        if self.code == code_input:
            Addons.slow_print("\nPodałeś właściwy Kod!\n", 0.05, newline=False)
            player.update_lvl(50)
            self.fight_with_boss(player)
            return True

        else:
            Addons.slow_print("\nZły kod.\nZ podłogi wysuwają się kłujące kolce.\n", 0.05, newline=False)
            player.update_hp(10)
            if not player.dead:
                input("\nWciśnij ENTER, aby kontunuować...")
            else:
                return True

        return False

    def fight_with_boss(self, player):
        Addons.slow_print("Wrota otwierają się z wielkim piskiem...\n" + self.boss_name + " chce pożreć Twoją duszę!",
                          0.1)
        Addons.slow_print(self.boss_pict, 0.0001)
        input("\nWciśnij ENTER, aby kontunuować...")

        player.fight(self.boss_name, int(self.score_multiplier * player.max_hp / 9) * 10)
        if not player.dead:
            Addons.slow_print("Teraz już nic nie stoi na przeszkodzie, aby opuścić to miejsce.\nOdzyskałeś wolność...",
                              0.05)
            Addons.print_congrats()
            print("\nKONIEC GRY")
            player.save_score(self.score_multiplier)
            input("\nWciśnij ENTER, aby kontunuować...")
        os.system('cls')

    def load_boss(self, player_class):
        self.boss_name = ['Deathwing', 'Czarnoksieznik', 'Ksiezniczka'][int(player_class) - 1]
        self.boss_pict = ""

        with open("boss.txt", "r") as f:
            tmp = 0
            for line in f:
                if line.startswith("x x"):
                    tmp += 1
                if tmp > int(player_class)*2:
                    break
                if tmp > int(player_class)*2 - 2:
                    self.boss_pict += line
