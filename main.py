from classes.game import Person, bcColor
from classes.Magic import Spell
from classes.inventory import Item

# Black Magic
fire = Spell("Fire", 15, 200, "Black")
thunder = Spell("Thunder", 10, 150, "Black")
blizzard = Spell("Blizzard", 8, 125, "Black")
meteor = Spell("Meteor", 6, 100, "Black")
quake = Spell("Quake", 4, 80, "Black")
wind = Spell("Wind", 2, 70, "Black")

# White Magic
cure = Spell("Cure", 10, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# Create Item
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hiPotion = Item("HiPotion", "potion", "Heals 100 HP", 100)
superPotion = Item("SuperPotion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restore HP/MP of one party member", 9999)
megaElixer = Item("MegaElixer", "elixer", "Fully restore party's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

playerSpells = [fire, thunder, blizzard, meteor, quake, wind, cure, cura]
# playerItem = [potion, hiPotion, superPotion, elixer, megaElixer, grenade]
playerItem = [
    {"item": potion, "quantity": 15},
    {"item": hiPotion, "quantity": 5},
    {"item": superPotion, "quantity": 5},
    {"item": elixer, "quantity": 5},
    {"item": megaElixer, "quantity": 2},
    {"item": grenade, "quantity": 5},
]

player = Person(460, 65, 60, 34, playerSpells, playerItem)
enemy = Person(1200, 65, 45, 25, [], [])
running = True
i = 0

print(bcColor.FAIL + bcColor.BOLD + "ENEMY ATTACKS!" + bcColor.ENDC)
while running:
    print("===================================")
    player.actionPick()
    pPick = input("Pick Action: ")
    indexPpick = int(pPick) - 1
    if indexPpick == 0:
        dmg = player.generateDamage()
        enemy.takeDamage(dmg)
        print("You Attacked for ", dmg, " points of damage.     Enemy HP: ")
    elif indexPpick == 1:
        player.MagicPick()
        magicPick = int(input("Pick Action: ")) - 1
        if magicPick == -1:
            continue

        spell = player.magic[magicPick]
        magicDmg = spell.generateSpellDamage()

        currnetMagicPoint = player.getMagicPoint()
        if spell.cost > currnetMagicPoint:
            print(bcColor.FAIL + "\nNot enough Magic Points\n" + bcColor.ENDC)
            continue
        player.reduceMagicPoint(spell.cost)

        if spell.type == "White":
            player.heal(magicDmg)
            print(bcColor.OKBLUE + "\n" + spell.name + " heals for ", str(magicDmg), " hit points. " + bcColor.ENDC)
        elif spell.type == "Black":
            enemy.takeDamage(magicDmg)
            print(bcColor.OKBLUE + "\n" + spell.name + " deals ", str(magicDmg), " points of damage " + bcColor.ENDC)
    elif indexPpick == 2:
        player.ItemPick()
        itemPick = int(input("Pick Item ")) - 1
        if itemPick == -1:
            continue
        item = player.items[itemPick]["item"]
        if player.items[itemPick]["quantity"] == 0:
            print(bcColor.FAIL + "\n" + " Out of items " + bcColor.ENDC)
            continue
        player.items[itemPick]["quantity"] -= 1


        if item.type == "potion":
            player.heal(item.prop)
            print(bcColor.OKGREEN + "\n" + item.name + " heals for ", str(item.prop), " hp " + bcColor.ENDC)
        elif item.type == "elixer":
            player.hitPoint = player.maxHitPoint
            player.magicPoint = player.maxMagicPoint
            print(bcColor.OKGREEN + "\n" + item.name + " fully restores MP/HP " + bcColor.ENDC)
        elif item.type == "attack":
            enemy.takeDamage(item.prop)
            print(bcColor.FAIL + "\n" + item.name + " deals ", str(item.prop), " points of damage" + bcColor.ENDC)

    ePick = 1
    edmg = enemy.generateDamage()
    player.takeDamage(edmg)
    print("Enemy Attacked for ", edmg, " points of damage.     Enemy HP: ")

    print("-------------------------------------------------------------------")
    print("Enemy Hit Point: ",
          bcColor.FAIL + str(enemy.getHitPoint()) + "/" + str(enemy.getMaxHitPoint()) + bcColor.ENDC + "\n")
    print("Your Hit Point: ",
          bcColor.OKBLUE + str(player.getHitPoint()) + "/" + str(player.getMaxHitPoint()) + bcColor.ENDC)
    print("Your magic Points: ",
          bcColor.OKGREEN + str(player.getMagicPoint()) + "/" + str(player.getMaxMagicPoint()) + bcColor.ENDC + "\n")

    if enemy.getHitPoint() == 0:
        print(bcColor.OKBLUE + " You Won " + bcColor.ENDC)
        running = False
    elif player.getHitPoint() == 0:
        print(bcColor.FAIL + " Enemy has defeated you " + bcColor.ENDC)
        running = False
