#############################
# Dice Randomizer in Python #
#############################

import random

# Variables
D4 = 5
D6 = 7
D8 = 9
D10 = 11
D12 = 13
D20 = 21
DP = 101

# Epic phrases for the cool kids B)
phrases = [
    "Here we go!",
    "Come on, baby!",
    "Don't fail me now!",
    "Yabba-dabba-doo!",
    "Poggers!",
    "Bombs away!",
    "Let luck be a lady tonight!",
    "Papa needs to slay an orc!",
    "Big money, no whammy!",
    "I HAVE THE POWER!!!",
    "Please be nice!",
    "I can has big roww pwease? OwO",
    "Crits be in the air tonight!",
    "Berries and cream!",
    "Show me the money!",
    "To infinity and beyond!",
    "Shaken, not stirred.",
    "Go ahead, make my day!",
    "Here's lookin' at you, kid!",
    "Heeeeeeeeeere's Johnny!",
    "May the Force be with you!",
    "Say hello to my little friend!"
]
while True:
    print("Please enter the type of dice you're rolling. \n(D4, D6, D8, D10, D12, D20, or DP for Percentile Dice. Exit to quit.)")
    answer = input().lower()
    if answer == "d4":
        phraseChoice = random.randrange(0,len(phrases))
        diceRoll = random.randrange(1, D4)
        print("")
        print(phrases[phraseChoice]," \nYour roll is ", diceRoll, "!\n")
    elif answer == "d6":
        phraseChoice = random.randrange(0,len(phrases))
        diceRoll = random.randrange(1, D6)
        print("")
        print(phrases[phraseChoice]," \nYour roll is ", diceRoll, "!\n")
    elif answer == "d8":
        phraseChoice = random.randrange(0,len(phrases))
        diceRoll = random.randrange(1, D8)
        print("")
        print(phrases[phraseChoice]," \nYour roll is ", diceRoll, "!\n")
    elif answer == "d10":
        phraseChoice = random.randrange(0,len(phrases))
        diceRoll = random.randrange(1, D10)
        print("")
        print(phrases[phraseChoice]," \nYour roll is ", diceRoll, "!\n")
    elif answer == "d12":
        phraseChoice = random.randrange(0,len(phrases))
        diceRoll = random.randrange(1, D12)
        print("")
        print(phrases[phraseChoice]," \nYour roll is ", diceRoll, "!\n")
    elif answer == "d20":
        phraseChoice = random.randrange(0,len(phrases))
        diceRoll = random.randrange(1, D20)
        print("")
        print(phrases[phraseChoice]," \nYour roll is ", diceRoll, "!\n")
        if diceRoll == 1:
            print("NATURAL 1! CRITICAL FAIL!\n")
        elif diceRoll == 20:
            print("NATURAL 20! CRITICAL HIT!\n")
    elif answer == "dp":
        phraseChoice = random.randrange(0,len(phrases))
        diceRoll = random.randrange(1, DP)
        print("")
        print(phrases[phraseChoice]," \nYour roll is ", diceRoll, "!\n")
    elif answer == "exit":
        break