import random


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.damage = dmg
        self.type = type


    def generateSpellDamage(self):
        magicLow = self.damage - 15
        magicHigh = self.damage + 15
        return random.randrange(magicLow, magicHigh)

