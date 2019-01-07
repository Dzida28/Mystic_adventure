class Weapon:
    def __init__(self, name, dmg, chance, crit, attack_name):
        self.name = name
        self.dmg = dmg
        self.chance = chance
        self.crit = crit
        self.attack_name = attack_name

    def __str__(self):
        return "   (dmg %s-%s, chance %s%%, crit %s%%)" % (
            self.dmg - 10, self.dmg + 10,
            self.chance,
            self.crit
        )


class Armor:
    def __init__(self, name, armor):
        self.armor = armor
        self.name = name

    def __str__(self):
        return "%s    (redukcja obrażeń %s%%)" % (self.name, self.armor)
