# -*- coding: utf-8 -*-
import random
from Room import Room
from Action import Action


class Load:
    def __init__(self):
        self.room = Room()
        self.action = []

    def load(self, file, code):
        self.room = Room()
        self.action = []

        with open(file, "r", encoding='utf-8') as f:
            data = f.readlines()

        data = self.format_text(data)
        self.prepare_start_room(data[0], data[1])

        for i in range(2, len(data)-1, 23):
            self.room.add_room(data[i], data[i+1], data[i+2])
            self.action.append(Action(code))
            self.read_actions(data, i)

        self.shuffle_rooms()
        self.room.start(code.get_code_digit())

    def prepare_start_room(self, name, description):
        name = name[name.index("#") + 1:]
        self.room.add_room(name, description, "To jest pokój startowy. Nie ma tu nic ciekawego")

    def read_actions(self, data, i):
        for x in range(3, 23, 5):
            try:
                self.action[len(self.action)-1].add_action(data[i+x],
                                                           data[i+x+1], int(data[i+x+2]),
                                                           int(data[i+x+3]), data[i+x+4])
            except ValueError as error:
                input(error)
                exit(0)
        self.action[len(self.action) - 1].randomize()

    def shuffle_rooms(self):
        names = []
        doors = []
        descriptions = []
        actions = []

        names.append(self.room.rooms_names[0])
        doors.append(self.room.rooms_doors[0])
        descriptions.append(self.room.rooms_description[0])

        order = list(range(1, len(self.action) + 1))
        random.shuffle(order)

        for i in order:
            names.append(self.room.rooms_names[i])
            doors.append(self.room.rooms_doors[i])

            if order.index(i) > 5:
                descriptions.append(self.room.rooms_description[i] +
                                    "\nZamiast kolejnych drzwi, widzisz przed sobą portal.")
            else:
                descriptions.append(self.room.rooms_description[i])
            actions.append(self.action[i - 1])

        self.room.rooms_names = names
        self.room.rooms_doors = doors
        self.room.rooms_description = descriptions
        self.action = actions

    @staticmethod
    def format_text(lines):
        for i in range(len(lines)):
            lines[i] = lines[i].replace("\n", "")
            lines[i] = lines[i].replace("\\n", "\n")
            lines[i] = lines[i].replace("\r", "")
        return lines
