import os, random, string
os.system("cls")

# Beschrijving:
# Maak een programma die een wachtwoord van 24 tekens genereerd.
# Het wachtwoord moet aan de volgende eisen voldoen:
#       2 tot 6 hoofdletters.
#       Minimaal 8 kleine letters.
#       3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
#       De speciale tekens mogen niet op de eerste of laatste positie staan en ook niet op een vaste plek.
#       4 tot 7 cijfers (0 t/m 9).
#       Op de eerste 3 posities mag geen cijfer staan.

# Description:
# Create a program that generates a password with 24 letters/digits/special_signs.
# Rules:
#       2 to 6 upper letters
#       At least 8 lower letters
#       Exactly 3 signs from the following list: @ # $ % & _ ?
#       Special signs can't be at the first and/or last position
#       4 to 7 digits (0 to 9)
#       Digits can't be at the first 3 positions.

alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)
numbers = list(string.digits)
special_signs = ['@', '#', '$', '%', '&', '_', '?']

def passwordgenerator():
    # Randomize the amount of every character which is to be involved.
    alphabet_upper_amount = random.randint(2, 6)
    numbers_amount = random.randint(4, 7)
    special_signs_amount = 3
    # Calculating how many lower letters are necessary to fill up to 24 characters.
    alphabet_lower_amount = 24 - 4 - alphabet_upper_amount - numbers_amount - special_signs_amount
    # Start adding random characters in order according to the randomized amounts calculated earlier.
    random_characters = random.choice(alphabet_upper)
    for i in range(alphabet_upper_amount - 1):
        random_characters += random.choice(alphabet_upper)
    for x in range(numbers_amount):
        random_characters += random.choice(numbers)
    for y in range(special_signs_amount):
        random_characters += random.choice(special_signs)
    for z in range(alphabet_lower_amount):
        random_characters += random.choice(alphabet_lower)
    # Orderly randomized characters are made into a list and shuffled. After shuffle, list is reverted to string.
    random_character_list = list(random_characters)
    random.shuffle(random_character_list)
    random_character_string = ''.join(random_character_list)
    # Adds the 3 fixed lowered letters and adds the other randomized string to it. After, one more fixed lowered letter is added.
    random_password = random.choice(alphabet_lower)
    for k in range(2):
        random_password += random.choice(alphabet_lower)
    random_password += random_character_string
    random_password += random.choice(alphabet_lower)
    # Returns the final password.
    password = random_password
    return password
# Executing the function 3 times to prove correct randomization and that the password meets the criteria.
print('Password 1: ', passwordgenerator())
print('\nPassword 2: ', passwordgenerator())
print('\nPassword 3: ', passwordgenerator())

# Code length - empty lines - commented lines = 31 (if only first execution counts 29)