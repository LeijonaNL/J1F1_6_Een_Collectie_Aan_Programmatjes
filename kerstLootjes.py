from os import system
from random import shuffle
import time
system("cls")
bar = "----------"

amount = int(input(f"How many names would you like to add?\n{bar}\n"))
names = []
tickets = []
for i in range(1, amount+1):
    name = input(f"{bar}\nPlease enter name {i}\n{bar}\n")
    names.append(name)
    tickets.append(name)
    shuffle(tickets)

shuffling = True
while shuffling: # There is a lower rotation with a sleep but you can also delete them and make it that it only prints the final outcome.
    shuffling = False
    shuffle(tickets)
    print(names)
    print(tickets, "\n")
    for x in range(1, amount+1):
        if names[x-1] == tickets[x-1]:
            time.sleep(0.5)
            shuffling = True