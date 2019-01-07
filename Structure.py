# -*- coding: utf-8 -*-
from Load import Load
import os


class Structure:
    def __init__(self, player, file, code):
        self.id_room = 1
        self.visited_room = []
        self.end = False
        self.player = player
        self.code = code
        self.load = Load()
        self.load.read_file(file, code)

    def p_move(self):
        sec = 0

        if self.id_room not in self.visited_room:
            self.visited_room.append(self.id_room)
            sec = 0.001

        while True:
            os.system('cls')
            available_moves = dict()

            self.load.room.introduce(self.id_room - 1, sec)
            print("-"*20 + "\nGdzie się ruszasz?\n")

            number = 1
            if self.id_room < 8:
                print("%s. %s" % (number, self.load.room.rooms_doors[self.id_room*2 + - 1]))
                available_moves[number] = self.go_left
                number += 1
                print("%s. %s" % (number, self.load.room.rooms_doors[self.id_room*2]))
                available_moves[number] = self.go_right
            else:
                print("%s. Wejdź do portalu" % number)
                available_moves[number] = self.approach_portal
            number += 1

            if self.id_room > 1:
                print("%s. Zawróć" % number)
                available_moves[number] = self.go_back
                number += 1
            print("\nLub...\n")

            if self.id_room > 1 and not all(self.load.action[self.id_room - 2].done):
                print("%s. Wykonaj akcje" % number)
                available_moves[number] = self.do_action
                number += 1

            print("%s. Pokaż statystyki gracza\n" % number)
            available_moves[number] = self.player.show_equipment

            move = input(">>>")

            try:
                move = int(move)
                if move in list(map(lambda a: a + 1, range(number))):
                    available_moves.get(move)()
                    break
            except ValueError:
                pass
            finally:
                sec = 0

    def go_left(self):
        self.id_room = self.id_room*2

    def go_right(self):
        self.id_room = self.id_room*2 + 1

    def go_back(self):
        self.id_room = int(self.id_room/2)

    def do_action(self):
        self.load.action[self.id_room-2].do_action(self.player, self.load.room, self.id_room - 1)

    def approach_portal(self):
        if self.code.game_end(self.player):
            self.end = True
        else:
            self.id_room = 1
