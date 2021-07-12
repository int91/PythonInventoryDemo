import globals as g

def drawInventory():
    if (len(g.inventory) < 10*g.inventoryPage):
        for i in range(10*(g.inventoryPage-1), len(g.inventory)):
            print("[" + str(i+1) + "] " + g.inventory[i])
            pass
    else:
        for i in range(10*(g.inventoryPage-1)+1, 10*g.inventoryPage+1):
            j = i-1
            print("[" + str((i)) + "] " + g.inventory[j])
            pass
    pass

def drawActions(item):
    print(item)
    print("[1] Use")
    print("[2] Equip")
    print("[3] Discard")
    choice = input("-> ")
    if (choice.isnumeric()):
        choice = int(choice)
        if (choice == 1):
            print("Used " + item)
        elif (choice == 2):
            print("Equipped " + item)
        elif (choice == 3):
            print("Discarded " + item)
            g.inventory.remove(item)
        else:
            drawActions(item)
    elif (choice == "back" or choice == "b"):
        menu()
    elif (choice == "q" or choice == "quit"):
        exit()
    else:
        drawActions(item)
    pass

def menu():
    global inventoryPage
    drawInventory()
    choice = input("-> ")
    if (choice.isnumeric()):
        choice = int(choice)
        if (choice <= len(g.inventory)):
            drawActions(g.inventory[choice-1])
        pass
    pass
    if (choice == "n"):
        g.inventoryPage += 1
        menu()
    elif (choice == "b"):
        g.inventoryPage -= 1
        menu()
    elif (choice == "q" or choice == "quit"):
        exit()
    else:
        menu()
    pass

menu()
