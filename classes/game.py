import random


class bcColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, mg):
        self.maxHitPoint = hp
        self.hitPoint = hp
        self.maxMagicPoint = mp
        self.magicPoint = mp
        self.attackHigh = atk + 10
        self.attackLow = atk - 10
        self.defense = df
        self.magic = mg
        self.action = ["Attack", "Magic"]

    def generateDamage(self):
        return random.randrange(self.attackLow, self.attackHigh)

    def generateSpellDamage(self, s):
        magicLow = self.magic[s]["dmg"] - 5
        magicHigh = self.magic[s]["dmg"] + 5
        return random.randrange(magicLow, magicHigh)

    def takeDamage(self, dmg):
        self.hitPoint -= dmg
        if self.hitPoint < 0:
            self.hitPoint = 0
        return self.hitPoint

    def getHitPoint(self):
        return self.hitPoint

    def getMaxHitPoint(self):
        return self.maxHitPoint

    def getMagicPoint(self):
        return self.magicPoint

    def getMaxMagicPoint(self):
        return self.maxMagicPoint

    def reduceMagicPoint(self, cost):
        self.magicPoint -= cost

    def getSpellName(self, s):
        return self.magic[s]["name"]

    def getSpellCost(self, s):
        return self.magic[s]["cost"]

    def actionPick(self):
        i = 1
        print("Action")
        for item in self.action:
            print(str(i) + ":", item)
            i += 1

    def MagicPick(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], " (cost: ", str(spell["magicPoint"]+")"))
            i += 1
