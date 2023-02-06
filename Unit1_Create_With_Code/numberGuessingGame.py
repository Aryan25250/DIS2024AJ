import time
import random

numGuesses = 10
range1 = 1
range2 = 100

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

levelsBeat = []

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

        guess = int(input("Guess a number between "+str(thisRange1)+" and "+str(thisRange2)+": "))

        time.sleep(.2)

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        elif guess == number:
            won = True

            if not level in levelsBeat:
                levelsBeat.append(level)

            print("Congrats! You beat "+level+" mode! It took you "+str(i+1)+" guesses!")
            time.sleep(.5)
            break

        time.sleep(.2)

    if not won:
        print("You lost! The number was: "+str(number))

    response = input("Respond with 'yes' to play again: ")
    if response.lower() != "yes":
        quit()

def introduction():
    name = input("What's your name?: ")

    print("Hello, "+name+"! Welcome to the number guessing game!")

    time.sleep(1)

def getLevel():
    string = "\nWhich level would you like to play?\n\n"

    for i, (k,v) in enumerate(levels.items()):
        emoji = "❌"
        if k in levelsBeat:
            emoji = "✅"

        string += "("+str(i+1)+") "
        string += k + " "+emoji+"\n"

    chosenLevel = None
    while not chosenLevel:
        thisChosenLevel = input(string)

        if thisChosenLevel.capitalize() in levels:
            chosenLevel = thisChosenLevel.capitalize()

    return chosenLevel

def getAction():
    chosenAction = None

    while not chosenAction:
        thisAction = input("(1) Play\n(2) Scoreboard\n(3) Quit\n")

        if thisAction == "1" or thisAction.lower == "play":
            chosenAction = "Play"

introduction()

while True:
    action = getAction()

    level = getLevel()

    game(level,levels[level])
