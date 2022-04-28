# Boodschappenlijstje

# mogelijke producten, vragen of invullen
    # De gebruiker word gevraagd om een item aan het lijstje toe te voegen en na het toevoegen of er nog meer is toe te voegen.
    # Een item uit de boodschappen lijst bestaat uit 2 delen (wat en hoeveel)
    # Als een item 2x word opgegeven word deze maar 1 keer in het lijstje getoond met de totale hoeveelheid
    # Als de gebruiker geen boodschappen meer wilt toevoegen word het totale lijstje aan de gebruiker getoond.

    # The user will be asked to add an item to the list and after adding it if they want to add more or not.
    # An item from the ticket exists out of 2 parts(what and how many)
    # If an item is added twice or more, the key will be shown as 1 and the value is to be increased.
    # If the user doesn't want to add any more products (keys) a final ticket will be displayed.

import os, time
os.system("cls")

shopList = {

}

def addToCart(shopList):
    os.system("cls")
    addProduct = input("What product would you like to add to your cart? ").upper()
    addNumber = int(input(f'How many of "{addProduct}" would you like to add to your cart? '))
    if addProduct in shopList.keys():
        shopList[addProduct]+=addNumber
    else:
        shopList[addProduct]=addNumber
    return shopList

repeat = True
while repeat:
    repeat = False
    shopList2 = addToCart(shopList)
    invalid = True
    while invalid:
        invalid = False
        time.sleep(1)
        os.system("cls")
        for key, value in shopList2.items():
            print(key, "x", value)
        repeatQuestion = input("This is your current cart, would you like to add more to your cart or would you like to place your order?\n1. Add\n2. Continue\n").upper()
        if repeatQuestion == "1" or repeatQuestion == "ADD":
            repeat = True
        elif repeatQuestion == "2" or repeatQuestion == "CONTINUE":
            os.system("cls")
            print("Alright, here's your ticket.")
            print("----------\nTICKET\n----------\n")
            for key, value in shopList2.items():
                print(value, "x", key)
            print("\n----------\n")
            enter = input("Press enter to finish. ")
        else:
            print("Sorry, this input is invalid, please try again.")
            invalid = True