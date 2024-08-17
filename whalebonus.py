def whalebonus(choice : str, player : list, cards : list, relics : list) :
    match choice:
        case "2":
            player[1] += 8
            print("Added 8 Max HP!\n")
        case "3":
            cards.append("Curse")
            cards.append("Strike+")
            print("Got a Strike+!\n")
        case "4":
            relics.remove("Burning Blood")
            relics.append("Snecko Eye")
            print("Got Snecko Eye!\n")