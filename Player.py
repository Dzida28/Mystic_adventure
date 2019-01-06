﻿# -*- coding: utf-8 -*-
import os
import random
import time
import pickle
import Addons
from Items import Weapon
from Items import Armor
from functools import reduce


class Player:
    def __init__(self, max_hp, code):
        self.exp = 0
        self.lvl = 1
        self.max_hp = max_hp
        self.hp = self.max_hp
        self.dead = False
        self.weapon = []
        self.armor = []
        self.available_weapons = []
        self.available_attack_names = []
        self.available_armors = []
        self.code = code

    def fight(self, enemy_name, full_enemy_hp):
        enemy_hp = full_enemy_hp

        while True:
            time.sleep(0.05)
            p = -1
            while not (0 <= p < len(self.weapon)):
                os.system('cls')
                print("-"*20)
                Addons.slow_print("Hp Gracza: " + str(self.hp) + "\nHp przeciwnika: " + str(enemy_hp), 0.005)

                for x in range(0, len(self.weapon)):
                    print("%s. %s" % (x + 1, self.weapon[x]))

                print("\nPodaj numer ataku")
                p = input(">>>")

                try:
                    p = int(p)
                    p -= 1
                except ValueError:
                    p = -1

            print("...")
            if random.randint(0, 100) < self.weapon[p].chance:
                if random.randint(1, 100) > self.weapon[p].crit:
                    tmp = self.weapon[p].dmg + random.randint(-10, 10)
                else:
                    Addons.slow_print("Obrażenia krytyczne!", 0.05)
                    tmp = (self.weapon[p].dmg + random.randint(-10, 10))*2
                enemy_hp -= tmp
                Addons.slow_print("Trafiłeś za " + str(tmp), 0.05)

            else:
                Addons.slow_print("\nChybiłeś", 0.05)

            if enemy_hp <= 0:
                tmp = random.randint(int(full_enemy_hp * (self.lvl / 10 + 1)) - 40,
                                     int(full_enemy_hp * (self.lvl / 10 + 1)))
                Addons.slow_print("Wygrałeś!", 0.05)
                self.update_lvl(tmp)
                break

            tmp = int(random.randint(5, 25) * ((self.lvl/5) + 1))
            Addons.slow_print(enemy_name + " atakuje Cię!", 0.01)
            self.update_hp(tmp)
            if self.dead:
                break

            input("\n\nWciśnij ENTER, aby kontynuować...")

    def update_lvl(self, value):
        time.sleep(0.05)
        level_up = False
        old_max_hp = self.max_hp
        value = int(value * (self.lvl/4 + 0.75))

        self.exp += value
        Addons.slow_print("Dostałeś " + str(value) + " exp", 0.05)

        while self.exp >= self.lvl*100:
            self.exp -= self.lvl*100
            self.lvl += 1
            self.max_hp += 10
            level_up = True

        if level_up:
            print("*"*20)
            Addons.slow_print("Nowy poziom!\nTwój poziom: %s\nJesteś w pełni wyleczony."
                              "\nTwój maksymalny poziom hp został zwiększony o %s"
                              % (self.lvl, (self.max_hp - old_max_hp)), 0.05)
            self.hp = self.max_hp
        else:
            Addons.slow_print("Brakuje Ci " + str(self.lvl * 100 - self.exp) + " exp do nowego poziomu", 0.05)

    def update_hp(self, value):
        time.sleep(0.05)

        dmg_reduction = 0
        for x in self.armor:
            dmg_reduction += x.armor
        if value > 0:
            value = int(value*(100 - dmg_reduction)/100)

        self.hp -= value
        if self.hp <= 0:
            self.hp = 0
            Addons.slow_print("Tracisz " + str(value) + " hp", 0.005)
            print("[*] RIP [*]\n")
            Addons.print_gameover()
            self.save_score()
            self.dead = True
            input("\nWciśnij ENTER, aby kontunuować...")

        elif value > 0:
            Addons.slow_print("Tracisz %s hp, pozostało Ci %s/%s hp." % (value, self.hp, self.max_hp), 0.05)

        elif value < 0:
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            Addons.slow_print("Zostajesz uleczony o %s hp, masz %s/%s hp." % (abs(value), self.hp, self.max_hp), 0.05)

    def add_armor(self, name, armor):
        self.armor.append(Armor(name, armor))

    def add_weapon(self, name, dmg, chance, crit, attack_name):
        self.weapon.append(Weapon(name, dmg, chance, crit, attack_name))

    def add_random_weapon(self):
        if self.available_weapons:
            index = random.randint(0, len(self.available_weapons) - 1)
            name = self.available_weapons.pop(index)
            dmg = random.randint(self.lvl + 3, self.lvl + 6) * 10
            chance = random.randint(50, 90)
            crit = random.randint(self.lvl + 1, self.lvl + 15)
            attack_name = self.available_attack_names.pop(index)
            self.add_weapon(name, dmg, chance, crit, attack_name)
            Addons.slow_print("Otrzymujesz przedmiot: %s" % self.weapon[-1], 0.05)

    def add_random_armor(self):
        if self.available_armors:
            name = self.available_armors.pop(random.randint(0, len(self.available_armors) - 1))
            armor = random.randint(2, 7)*2
            self.add_armor(name, armor)
            Addons.slow_print("Otrzymujesz przedmiot: %s" % self.armor[-1], 0.05)

            while True:
                dmg_reduction = reduce(lambda a, x: a + x.armor, self.armor, 0)

                if dmg_reduction >= 80:
                    Addons.slow_print("Jesteś przeciążony. Musisz pozbyć się przedmiotu %s" % self.armor[0], 0.05)
                    del self.armor[0]
                else:
                    break

    def load_weapons(self, amount):
        with open("weapon.txt", encoding='utf-8') as f:
            lines = []
            tmp = 1
            for i, line in enumerate(f):
                if "..." in line:
                    tmp += 1
                if tmp > amount:
                    break

                if tmp > amount - 1 and "..." not in line:
                    lines.append(line.replace("\n", ""))

            if amount == 1:
                lines[0] = lines[0][lines[0].index("#") + 1:]
            for i in range(0, len(lines) - 1, 3):
                self.available_weapons.append(lines[i])
                self.available_attack_names.append(lines[i+1])
                self.available_armors.append(lines[i+2])

    def show_equipment(self):
        os.system('cls')
        print("-"*20)
        Addons.slow_print("Statystyki gracza:\n", 0.02, newline=False)
        Addons.slow_print("Poziom: %s\n" % self.lvl, 0.01, newline=False)
        Addons.slow_print("Hp: %s/%s\n" % (self.hp, self.max_hp), 0.01, newline=False)
        Addons.slow_print("Exp: %s/%s\n\n" % (self.exp, self.lvl * 100), 0.01, newline=False)

        print("-"*20 + "\nEkwipunek:")
        if self.weapon:
            for x in range(1, len(self.weapon)):
                print("%s. %s" % (x, self.weapon[x]))
                time.sleep(0.2)
            print("...")

        if self.armor:
            for x in range(0, len(self.armor)):
                print("%s. %s" % (len(self.weapon) + x, self.armor[x]))
                time.sleep(0.2)
            Addons.slow_print("Łączna redukcja obrażen: %s%%\n" %
                              reduce(lambda a, b: a + b.armor, self.armor, 0),
                              0.01, newline=False)
            print("...")

        print(str(len(self.weapon) + len(self.armor)) + ". Kartka z zapisanym kodem: " + self.code.return_known_code())
        input("\n\n\nWciśnij ENTER, aby kontunuować...")

    def save_score(self, multiple=1):
        if not os.path.isfile("scores.dat"):
            with open("scores.dat", "wb") as file:
                pickle.dump([0, 0, 0], file)

        score = self.exp
        for i in range(self.lvl + 1):
            score += i*100
        score -= 100
        score += (len(self.weapon) - 2)*50 + (len(self.armor) - 1)*50
        score += int(self.hp*multiple)
        score = int(score*multiple)

        print("\nZdobyłeś %s punktów!\n" % score)

        with open("scores.dat", "rb") as file:
            all_scores = pickle.load(file)

        all_scores.append(score)
        all_scores.sort(reverse=True)

        print("Tabela wyników:")
        for i in range(0, 3):
            print(str(i + 1) + ". " + str(all_scores[i]))

        if all_scores[3] == score and not all_scores[2] == score:
            print("...\n4. " + str(score))

        all_scores.remove(all_scores[3])

        file = open("scores.dat", "wb")
        pickle.dump(all_scores, file)
        file.close()
