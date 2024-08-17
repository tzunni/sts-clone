from random import sample
from cards import *
from collections import Counter
from enemy import enemyturn
import os
def gameloop(player : list, cards : list, relics : list, enemies : list) :
    drawpile = Counter(cards)
    hand = []
    while len(enemies) != 0:
        # player turn
        print("Player turn!")
        mana = [3]
        block = [0]
        if "Snecko Eye" in relics :
            snecko = True
        else:
            snecko = False
        if drawpile.total() >= 6 :
            hand = sample(list(drawpile.elements()), 6)
            drawpile -= Counter(hand)
        else :
            hand = sample(list(drawpile.elements()), drawpile.total())
            drawpile = Counter(cards)
            drawpile -= Counter(hand)
            buffersize = 6 - len(hand)
            buffer = sample(list(drawpile.elements()), buffersize)
            hand += buffer
            drawpile = Counter(drawpile) - Counter(buffer)
        move = ""
        costs = []
        for card in hand :
            match card:
                case "Strike":
                    costs.append(1)
                case "Strike+":
                    costs.append(1)
                case "Defend":
                    costs.append(1)
                case "Defend+":
                    costs.append(1)
                case "Bash":
                    costs.append(2)
                case "Curse":
                    costs.append(0)
        if snecko :
            for index, cost in enumerate(costs):
                a = randint(0, 4) - 2
                costs[index] += a
                if costs[index] < 0 :
                    costs[index] = 0
        while(True):
            if (len(enemies)) == 0:
                break
            headsup(player, block, enemies, hand, mana)
            playerstate = play(hand, move, enemies, block, mana, costs)
            for enemy in enemies :
                if enemy[1] <= 0 :
                    enemies.remove(enemy)
            if playerstate == False :
                break
        while(True):
            if (len(enemies)) == 0:
                break
            headsup(player, block, enemies, hand, mana)
            enemystate = enemyturn()
            if enemystate == False :
                break

def headsup(player : list, block : int, enemies : list, hand : list, mana : list) :
    print(f'\033[1m{player[0]}\033[0m:{player[1]}❤️, {block[0]}🛡️, 🔮:{mana[0]}')
    enemystr = ""
    for enemy in enemies :
        enemystr += (f'\033[1m{enemy[0]}\033[0m:{enemy[1]}❤️, {enemy[3]}🛡️, {enemy[2]}💔 ')
    print(enemystr)