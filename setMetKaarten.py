# SET MET KAARTEN

import os, random

# Beschrijving
# Maak een programmatje die een standaard deck met kaarten genereerd (54 kaarten), deze schut en de bovenste 7 -
# er afhaald op het scherm toont en daarna de overige kaarten in het deck.
# De volgende regels gelden voor dit programma:
#     Het deck bestaat uit 4 “kleuren” (harten, klaveren, schoppen & ruiten)
#     Iedere kleur heeft 13 kaarten (2 t/m 10, een boer, een vrouw, een heer en een aas)
#     Er zitten ook 2 jokers in het deck
#     Als je geen User Defined Functions gebruikt bestaat je code uit minder dan 18 regels (exclusief lege regels)
#     Als je wel User Defined Functions gebruikt bestaat je code uit minder dan 28 regels (exclusief lege regels)

# Create a program that generates a standard deck with cards (54 cards), shuffles the cards and displays them on the screen together with the unused cards.
# Rules:
# Deck must exist out of 4 "colors" (in my case the "types" list).
# Every "color" must have all 13 cards ("cards" list)
# There must be 2 Jokers in the deck.
# If you don't use User Defined Functions the code should be less than 18 lines (unfilled lines exclusive)
# If you DO use User Defined Functions the code should be less that 28 lines (unfilled lines exclusive)

types = ['Harten', 'Klaveren', 'Schoppen', 'Ruiten']
cards = ['aas', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'koning', 'vrouw', 'boer']
deck, hand = [], []
for i in range(len(types)):
    if i % 2 == 0:
        deck.append('Joker')
    for x in range(len(cards)):
        deck.append(f'{types[i]} {cards[x]}')
deckSize = len(deck)
for y in range(7):
    handPick = random.choice(deck)
    hand.append(f'Kaart {y+1} = {handPick}')
    deck.remove(handPick)
    deckSize -= 1
    random.shuffle(deck)
print(*hand,sep='\n')
print(f'\ndeck ({len(deck)} kaarten):\n{deck}')