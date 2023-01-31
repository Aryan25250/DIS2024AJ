import time
import random

numGuesses = 10
range1 = 1
range2 = 100

def game():
    print("\nWelcome to the number guessing game!")
    time.sleep(.5)
    input("Respond with anything to start!: ")

    print("Generating number...")
    time.sleep(2)
    number = random.randint(range1,range2)

    for i in range(numGuesses):
        print("\n--GUESS "+str(i+1)+"/"+str(numGuesses)+"--\n")

        guess = int(input("Guess a number between "+str(range1)+" and "+str(range2)+": "))

        time.sleep(.2)

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        elif guess == number:
            print("Congrats! You won!")
            time.sleep(.5)
            break

        time.sleep(.2)

    response = input("Respond with 'yes' to play again: ")
    if response.lower() != "yes":
        quit()

while True:
    game()