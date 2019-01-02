# -*- coding: utf-8 -*-
import os
import Load
import Code


class Structure:
    def __init__(self, filename):
        self.id_room = 1
        self.print_fast_id = 0
        self.end = False
        Load.FILE = filename
        Load.load()
        os.system('cls')
        Load.room.start()

    def p_move(self, player):
        if self.print_fast_id != self.id_room:
            sec = 0.001
            self.print_fast_id = self.id_room
        else:
            sec = 0

        while True:
            os.system('cls')
            Load.room.introduce(self.id_room - 1, sec)
            print("-" * 20 + "\n\nGdzie się ruszasz?\n")

            if self.id_room < 8:
                print("1. " + Load.room.rooms_doors[self.id_room * 2 + - 1])
                print("2. " + Load.room.rooms_doors[self.id_room * 2])

                if self.id_room > 1:
                    print("3. Zawróć")
                    if not all(Load.action[self.id_room - 2].done):
                        print("\nLub...\n4. Wykonaj akcje\n5. Pokaż statystyki gracza\n")
                    else:
                        print("\nLub...\n4. Pokaż statystyki gracza\n")
                else:
                    print("\nLub...\n3. Pokaż statystyki gracza\n")

                move = input(">>>")

                if move == "1":
                    self.id_room *= 2
                    break

                if move == "2":
                    self.id_room = self.id_room * 2 + 1
                    break

                if move == "3" and self.id_room == 1:
                    player.show_equipment()
                    break

                if self.id_room > 1:
                    if move == "3":
                            self.id_room = int(self.id_room / 2)
                            break

                    if move == "4":
                        if not all(Load.action[self.id_room - 2].done):
                            Load.action[self.id_room - 2].do_action(player, Load.room, self.id_room - 1)
                            self.print_fast_id = self.id_room
                            break
                        else:
                            player.show_equipment()

                if move == "5" and not all(Load.action[self.id_room - 2].done):
                    player.show_equipment()

            else:
                print("1. Wejdź do portalu")
                print("2. Zawróć")
                if not all(Load.action[self.id_room - 2].done):
                    print("\nLub...\n3. Wykonaj akcje\n4. Pokaż statystyki gracza\n")
                else:
                    print("\nLub...\n3. Pokaż statystyki gracza\n")

                move = input(">>>")

                if move == "1":
                    if Code.ending(player) == 1:
                        self.end = True
                        break
                    else:
                        self.id_room = 1
                        break

                if move == "2":
                    self.id_room = int(self.id_room / 2)
                    break

                if move == "3":
                    if not all(Load.action[self.id_room - 2].done):
                        Load.action[self.id_room - 2].do_action(player, Load.room, self.id_room - 1)
                        self.print_fast_id = self.id_room
                        break
                    else:
                        player.show_equipment()

                if move == "4" and not all(Load.action[self.id_room - 2].done):
                    player.show_equipment()

            self.print_fast_id = self.id_room
            sec = 0

    os.system('cls')
