from mechanics import *
from random import randint
def play(hand : list, move : int, enemies : list, block : list, mana : list, costs : list) :
    cardstr = "\n"
    for index, card in enumerate(hand) :
        cost = f"{costs[index]}🔮"
        if card == "Curse" :
            cost = "..."
        cardstr += (f'{card}:{cost} ')
    print(cardstr)
    print("Pick a card or end... ", end="")
    move = input()
    if move == "end" or move == '' :
        print("Enemy turn!")
        return False
    print(hand[int(move)])
    match hand[int(move)]:
        case "Strike":
            if mana[0] >= costs[int(move)] :
                print("Which one? ", end="")
                enemy = enemies[int(input())]
                attack(5, enemy)
                mana[0] -= costs[int(move)]
                hand.remove(hand[int(move)])
                costs.remove(costs[int(move)])
                print("")
            else :
                print("Not enough mana!\n")
        case "Strike+":
            if mana[0] >= costs[int(move)] :
                print("Which one? ", end="")
                enemy = enemies[int(input())]
                attack(8, enemy)
                mana[0] -= costs[int(move)]
                hand.remove(hand[int(move)])
                costs.remove(costs[int(move)])
                print("")
            else :
                print("Not enough mana!\n")
        case "Defend":
            if mana[0] >= costs[int(move)] :
                block[0] += shield(5)
                mana[0] -= costs[int(move)]
                hand.remove(hand[int(move)])
                costs.remove(costs[int(move)])
                print("")
            else :
                print("Not enough mana!\n")
        case "Defend+":
            if mana[0] >= costs[int(move)] :
                block[0] += shield(8)
                mana[0] -= costs[int(move)]
                hand.remove(hand[int(move)])
                costs.remove(costs[int(move)])
                print("")
            else :
                print("Not enough mana!\n")
        case "Bash":
            if mana[0] >= costs[int(move)]:
                print("Which one? ", end="")
                enemy = enemies[int(input())]
                attack(8, enemy)
                enemy[2] += 1
                mana[0] -= costs[int(move)]
                hand.remove(hand[int(move)])
                costs.remove(costs[int(move)])
                print("")
            else :
                print("Not enough mana!\n")
        case "Curse":
            print("Unplayable!\n")
    if len(enemies) == 0 :
        return False
    return True