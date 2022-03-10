from os import system
from random import shuffle, randint
from sys import stdout
from time import sleep
from collections import Counter
# Initial clear of run screen.
system("cls")
# Yahtzee

# Function to clear screen.
def clearScreen(sleepTime):
    sleep(sleepTime)
    system("cls")
# Preset bar to use in interface.
bar = '----------'
# key stands for the score number, value index 0 stands for if that number has already been used as a score or not, value index 1 stands for
# the total amount of points that dice number has gotten you.
scores = {
    1: [True, 0],
    2: [True, 0],
    3: [True, 0],
    4: [True, 0],
    5: [True, 0],
    6: [True, 0]
}
# Function for in the dices interface to show if a dice is locked or unlocked.
def un_Locked(value):
    if value:
        x = " Unlocked"
    else:
        x = " Locked  "
    return x
# Function for calculating the amount of dices you have for a certain dice number such as 3 times dices that rolled 6 and 2 times 4
def possible_Scores():
    numbers = Counter(x for _, x in dices.values())
    return numbers
# Function for displaying the dices, input is a randomized list, if value index 0 in dict dices is false a number in the input list won't be randomized again.
def fancyDice(*inDice):
    # Dices art
    diceDict = {
    1:{1:' ------- ',2:' ------- ',3:' ------- ',4:' ------- ',5:' ------- ',6:' ------- '},
    2:{1:'|       |',2:'| o     |',3:'| o     |',4:'| o   o |',5:'| o   o |',6:'| o   o |'},
    3:{1:'|   o   |',2:'|       |',3:'|   o   |',4:'|       |',5:'|   o   |',6:'| o   o |'},
    4:{1:'|       |',2:'|     o |',3:'|     o |',4:'| o   o |',5:'| o   o |',6:'| o   o |'},
    5:{1:' ------- ',2:' ------- ',3:' ------- ',4:' ------- ',5:' ------- ',6:' ------- '}
    }
    # Printing the dices art with stdout.write so that they add onto eachother nicely
    for i in range(5): #5 is for the 5 lines that de dice art requires
        for args in inDice:
            stdout.write(diceDict[i+1][args])
            stdout.write("   ")
        stdout.write("\n")
    # Printing the locked/unlocked part beneath the dices display in the interface, shows if dice is or isnt locked.
    for key, value in dices.items():
        un_locked = un_Locked(value[0])
        stdout.write(un_locked)
        stdout.write("   ")
    stdout.write("\n")
# Function for printing the scoreboard.
    # Scoreboard will most likely be unaligned on the right side, this can be fixed by using format but I'm not familiar enough to use it.
    # So I at least want to show that I know it's possible.
def scoreboard():
    print(f"                      \n\
            PLAYER                        \n\
            ________ _________ _________  \n\
           |PART 1  |  SCORE  |        | \n\
           |________|_________|_________| \n\
           |ACES    |TOTAL 1's|   {scores[1][1]}    | \n\
           |________|_________|_________| \n\
           |TWOS    |TOTAL 2's|   {scores[2][1]}    | \n\
           |________|_________|_________| \n\
           |THREES  |TOTAL 3's|   {scores[3][1]}    | \n\
           |________|_________|_________| \n\
           |FOURS   |TOTAL 4's|   {scores[4][1]}    | \n\
           |________|_________|_________| \n\
           |FIVES   |TOTAL 5's|   {scores[5][1]}    | \n\
           |________|_________|_________| \n\
           |SIXES   |TOTAL 6's|   {scores[6][1]}    | \n\
           |________|_________|_________| \n\
           |TOTAL POINTS ---->|   {total_points}    | \n\
           |__________________|_________| \n\
           |BONUS   |35POINTS |   {bonus}    | \n\
           |________|_________|_________| \n\
           |TOTAL ----------->|   {total_score}    | \n\
           |__________________|_________| \n\
           ")
# Presetting certain variables that don't have a starter value.
total_points = 0
total_score = 0
turns = 0
bonus = "-"
game = 0
# Main game code
while game < 6:
    turns += 1
    print(f"A new turn!\nThis is turn {turns}!")
    # Dict for rolling the dices, key stands for the individual dices, value index 0 stands for if the dice is allowed to be rolled or not
    # (locked or unlocked), value index 1 stands for the number that has been rolled for that specific dice.
    # Also resets every turn.
    dices = {
    1: [True, 0],
    2: [True, 0],
    3: [True, 0],
    4: [True, 0],
    5: [True, 0]
    }
    # Resetting throws every time you finish a turn.
    throws = 0
    while throws < 3:
        clearScreen(1)
        if throws > 0:
            fancyDice(*inDice_list)
        action = input(f"Player, what would you like to do?\n· Roll my dice(s)\n· Lock my dice(s)\n· Unlock my dice(s)\n· Look at the scoreboard\n· End my turn\n{bar}\n")\
            .upper().replace(" ", "").replace("MY", "").replace("AT", "").replace("THE", "").replace("LOOK", "").replace("DICE", "").replace("S", "").replace("TURN", "")
        # Code that randomizes the list that is used as input for the dices display, the numbers also get updated to the dices dict.
        if action == "ROLL":
            dices_list = []
            throws += 1
            for i in range(4):
                clearScreen(0.5)
                inDice_list = []
                for key_dice, value_dice in dices.items():
                    if value_dice[0]:
                        value_dice[1] = randint(1, 6)
                    inDice_list.append(value_dice[1])
                fancyDice(*inDice_list)
            dices_list.append
        # Code that allows you to lock a dice (put it aside), this makes them unable to be rolled again until it's unlocked.
        elif action == "LOCK":
            lock_question = True
            while lock_question:
                lock_question = False
                # toLock is which dice you want to be locked.
                toLock = int(input(f'Which dice would you like to lock in?\n{bar}\n'))
                dices[toLock][0] = False
                print(f"Dice number {toLock} has been locked.")
                clearScreen(1)
                fancyDice(*inDice_list)
                lockAgain = input(f"\nDo you want to lock another dice?\n· Yes\n· No\n{bar}\n").upper()
                if lockAgain == "YES":
                    lock_question = True
        # Code that allows you to unlock a dice (put it back), this makes them able to be rolled again.
        elif action == "UNLOCK":
            unlock_question = True
            while unlock_question:
                unlock_question = False
                # toUnlock is which dice you want to be unlocked.
                toUnlock = int(input(f"Which dice would you like to unlock?\nPlease respond with a number.\n{bar}\n"))
                dices[toUnlock][0] = True
                print(f"Dice number {toUnlock} has been unlocked.")
                clearScreen(1)
                fancyDice(*inDice_list)
                unlockAgain = input(f"\nDo you want to unlock another dice?\n· Yes\n· No\n{bar}\n").upper()
                if unlockAgain == "YES":
                    unlock_question = True
        # Code that adds the bonus if reached and also displays the scoreboard.
        elif action == "COREBOARD":
            clearScreen(0)
            if total_points >= 63:
                bonus = 36
            scoreboard()
            enter = input("Press ENTER to continue.")
        # Code that skips through the throws if you have your final line of dices you want to use.
        elif action == "END":
            throws = 3
        # In case something wrong was put in.
        else:
            print("I'm sorry I didn't understand that.")
    # Question what dice you want to use as a score for this turn.
    choise_question = True
    while choise_question:
        choise_question = False
        clearScreen(1)
        fancyDice(*inDice_list)
        numbers = possible_Scores()
        scoreboard()
        choise = int(input("What dice(s) do you want to use to score for this round?"))
        # If a dice has already been used to score with it won't be allowed to be reset/used again.
        if scores[choise][0] == False:
            choise_question = True
            print("That space has already been filled.")
            sleep(1.25)
            continue
        # To confirm your choise of dice for scoring with.
        confirm = input(f"\n{bar}\nAre you sure you want to use {choise} as a score this round?\n· Yes\n· No\n{bar}\n").upper()
        if confirm == "YES":
            scores[choise][0] = False
            scores[choise][1] = choise * numbers[choise]
            total_points += scores[choise][1]
            print(f"Alright! ...")
        elif confirm == "NO":
            choise_question = True
        else:
            print("I'm sorry I didn't understand that.")
            sleep(1.25)
    # Calculating the scores for dices and total to add onto the scoreboard after the turn.
    total_score = 0
    for key, value in scores.items():
        total_score += scores[key][1]
    if bonus == 36:
        total_score += bonus
    game += 1
# Last display of the scoreboard for once the code ends.\
clearScreen(1)
scoreboard()

