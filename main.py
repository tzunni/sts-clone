from whalebonus import whalebonus
from gameloop import *
player = ["Ironclad", 80]
cards = ["Strike", "Strike", "Strike", "Strike", "Strike", "Defend", "Defend", "Defend", "Defend", "Bash"]
relics = ["Burning Blood"]
print("Choose...\n\033[1;32mChoice 1: Transform a Card\nChoice 2: Max HP +8\nChoice 3: \033[1;31mObtain a curse, \033[1;32mgain a Strike+\nChoice 4: \033[1;31mLose your starting relic, \033[1;32mobtain Snecko Eye\033[0m")
choice = input()
whalebonus(choice, player, cards, relics)

# encounter 1
enemies = [["Red Louse", 10, 0, 0], ["Green Louse", 12, 0, 0]]
gameloop(player, cards, relics, enemies)

print("Congrats! You've completed the demo!")