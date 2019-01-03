# -*- coding: utf-8 -*-
import random
from Room import Room
from Action import Action


FILE = ""
room = Room()
action = []


def load():
    global room
    global action

    room = Room()
    action = []

    with open(FILE, "r", encoding='utf-8') as f:
        data = f.readlines()

    if len(data) == 324:
        for i in range(len(data)):
            data[i] = data[i].replace("\n", "")
            data[i] = data[i].replace("\\n", "\n")
            data[i] = data[i].replace("\r", "")

        data[0] = data[0][data[0].index("#") + 1:]
        room.add_room(data[0], data[1], "To jest pokój startowy. Nie ma tu nic ciekawego")

        for i in range(2, len(data)-1, 23):
            room.add_room(data[i], data[i+1], data[i+2])
            action.append(Action())

            for x in range(3, 23, 5):
                try:
                    action[len(action)-1].add_action(data[i+x], data[i+x+1], int(data[i+x+2]),
                                                     int(data[i+x+3]), data[i+x+4])
                except ValueError as error:
                    input(error)
                    exit(0)

            action[len(action)-1].randomize()

        names = []
        doors = []
        descriptions = []
        actions = []

        names.append(room.rooms_names[0])
        doors.append(room.rooms_doors[0])
        descriptions.append(room.rooms_description[0])

        order = list(range(1, len(action)+1))
        random.shuffle(order)

        for i in order:
            names.append(room.rooms_names[i])
            doors.append(room.rooms_doors[i])

            if order.index(i) > 5:
                descriptions.append(room.rooms_description[i] +
                                    "\nZamiast kolejnych drzwi, widzisz przed sobą portal.")
            else:
                descriptions.append(room.rooms_description[i])
            actions.append(action[i-1])

        room.rooms_names = names
        room.rooms_doors = doors
        room.rooms_description = descriptions
        action = actions
    else:
        input("Ktoś majstrowal przy plikach z danymi!")
        exit(0)
