def attack(dmg : int, enemy : list) :
    if enemy[2] > 0 :
        enemy[1] -= dmg * 1.5
    else :
        enemy[1] -= dmg

def shield(amt : int) -> int:
    return amt