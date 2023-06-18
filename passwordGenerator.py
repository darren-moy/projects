#This program generates a random password based on paramters inputted by the user
import random
import string


def generatePass(min_length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    passw = ""
    meetCriteria = False
    hasNum = False
    hasSpecial = False

    while not meetCriteria or len(passw) < min_length:
        new_char = random.choice(characters)
        passw += new_char

        if new_char in digits:
            hasNum = True
        elif new_char in special:
            hasSpecial = True

        meetCriteria = True
        if numbers:
            meetCriteria = hasNum
        if special_char:
            meetCriteria = meetCriteria and hasSpecial      #Ensures that it meets criteria

    return passw

while True:
    try:
        min_length = int(input("Enter the minimum length: "))
        break
    except ValueError:
        print("You did not enter a number. Please enter a number.")

hasNum = input("Do you want to have numbers (y/n)").lower() == "y"
hasSpecial = input("Do you want to have special characters (y/n)").lower() == "y"
passw = generatePass(min_length, hasNum, hasSpecial)
print(passw)




