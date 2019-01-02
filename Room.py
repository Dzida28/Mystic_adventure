# -*- coding: utf-8 -*-
import Addons
import Code


class Room:
    def __init__(self):
        self.rooms_names = []
        self.rooms_doors = []
        self.rooms_description = []

    def add_room(self, name, doors, description):
        self.rooms_names.append(name)
        self.rooms_doors.append(doors)
        self.rooms_description.append(description)

    def introduce(self, num, sec):
        print("-"*20)
        if self.rooms_names[num] != "Cmentarzu":
            Addons.slow_print("Jesteś w " + self.rooms_names[num], sec)
        else:
            Addons.slow_print("Jesteś na " + self.rooms_names[num], sec)
        Addons.slow_print(self.rooms_description[num], sec)

    def start(self):
        print("-" * 20)
        Addons.slow_print(self.rooms_doors[0], 0.001)
        Addons.slow_print("W kieszeni znajdujesz kartkę z napisem: " +
                          Code.get_code_digit() + "Masz przeczucie, że będzie to istotna informacja.", 0.001)
        input("\n\nWciśnij ENTER, aby kontynuować...")
