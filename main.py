from classes.game import Person, bcColor

magic = [
    {"name": "Fire", "cost": 10, "dmg": 60},
    {"name": "Thunder", "cost": 5, "dmg": 30},
    {"name": "Blizzard", "cost": 2, "dmg": 20},
]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)
running = True
i = 0

print(bcColor.FAIL+bcColor.BOLD +"ENEMY ATTACKS!" +bcColor.ENDC)
while running:
    print("===================================")
    player.actionPick()
    pPick=input("Pick Action: ")
    indexPpick=int(pPick)-1
    if indexPpick == 0:
        dmg = player.generateDamage()
        enemy.takeDamage(dmg)
        print("You Attacked for ", dmg, " points of damage.     Enemy HP: ", enemy.getHitPoint())

    ePick = 1
    edmg = enemy.generateDamage()
    player.takeDamage(edmg)
    print("Enemy Attacked for ", edmg, " points of damage.     Enemy HP: ", player.getHitPoint())

    # running = False

# print(player.generateDamage())
# print(player.generateDamage())
# print(player.generateDamage())
#
# print(player.generateSpellDamage(0))
# print(player.generateSpellDamage(1))
# print(player.generateSpellDamage(2))
