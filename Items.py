class Weapon:
    def __init__(self, name, dmg, chance, crit, attack_name):
        self.name = name
        self.dmg = dmg
        self.chance = chance
        self.crit = crit
        self.attack_name = attack_name


class Armor:
    def __init__(self, name, armor):
        self.armor = armor
        self.name = name
