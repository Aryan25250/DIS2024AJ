import time
import random

numGuesses = 10
range1 = 1
range2 = 100

scoreboard = {
    "Easy": [],
    "Medium": [],
    "Hard": [],
}

levels = {
    "Easy": {
        "numGuesses": 15,
        "range1": 1,
        "range2": 100,
    },
    "Medium": {
        "numGuesses": 10,
        "range1": 1,
        "range2": 250,
    },
    "Hard": {
        "numGuesses": 7,
        "range1": 1,
        "range2": 500,
    }
}

#ask for users name, respond hello name welcome
#at the end, tell how many guesses it took
#3 different levels (easy, medium, hard)
#high score table

def game(level,settings):
    thisRange1 = settings["range1"]
    thisRange2 = settings["range2"]
    thisNumGuesses = settings["numGuesses"]

    print("Generating number...")
    time.sleep(2)
    number = random.randint(thisRange1,thisRange2)

    won = False
    for i in range(thisNumGuesses):
        print("\n--GUESS "+str(i+1)+"/"+str(thisNumGuesses)+"--\n")

        guess = None

        while not guess:
            thisGuess = input("Guess a number between "+str(thisRange1)+" and "+str(thisRange2)+": ")

            try:
                thisGuess = int(thisGuess)
            except:
                print("That's not a valid number!")
            else:
                guess = thisGuess

        time.sleep(.2)

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        elif guess == number:
            won = True

            print("Congrats! You beat "+level+" mode! It took you "+str(i+1)+" guesses!\n")

            if i+1 not in scoreboard[level]:
                scoreboard[level].append(i+1)
            time.sleep(.5)
            break

        time.sleep(.2)

    if not won:
        print("You lost! The number was: "+str(number))

def scoreboardFunc():
    for i,(k,v) in enumerate(scoreboard.items()):
        print("--"+k.upper()+"--\n")

        v.sort()
        string = ""

        for x,y in enumerate(v):
            string += str(x+1)+") "+str(y)+"\n"

        print(string)

def introduction():
    name = input("What's your name?: ")
    print("Hello, "+name+"! Welcome to the number guessing game!\n")

    time.sleep(1)

def getLevel():
    string = "\nWhich level would you like to play?\n\n"

    levelsList = {}

    for i, (k,v) in enumerate(levels.items()):
        emoji = "❌"

        if len(scoreboard[k]) > 0:
            emoji = "✅"

        levelsList[i+1] = k

        string += "("+str(i+1)+") "
        string += k + " "+emoji+"\n"

    chosenLevel = None
    while not chosenLevel:
        thisChosenLevel = input(string)
        intLevel = None

        if thisChosenLevel.capitalize() in levels:
            chosenLevel = thisChosenLevel.capitalize()
        else:
            try:
                intLevel = int(thisChosenLevel)
            except:
                continue
            else:
                if intLevel in levelsList:
                    chosenLevel = levelsList[intLevel]

    return chosenLevel

def getAction():
    chosenAction = None

    while not chosenAction:
        thisAction = input("(1) Play\n(2) Scoreboard\n(3) Quit\n")

        if thisAction == "1" or thisAction.lower() == "play":
            chosenAction = "Play"
        elif thisAction == "2" or thisAction.lower() == "scoreboard":
            chosenAction = "Scoreboard"
        elif thisAction == "3" or thisAction.lower() == "quit":
            chosenAction = "Quit"

    return chosenAction

introduction()

while True:
    action = getAction()

    if action == "Quit":
        quit()
    if action == "Scoreboard":
        scoreboardFunc()
        continue

    level = getLevel()

    game(level,levels[level])