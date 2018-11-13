# By Jessica Angela Campisi
# Guess My Number
# 10/1/2018
# Description: The player will guess a number between 1 and 100. The computer will let them know if they are high or
# low.

# Imports
import random, sys

# Variables
random.seed()
randnum = random.randrange(1, 100)
playerGuess = 0
lastGuess = 0
count = 0
playerWin = False

# Testing Random
#print("Random number: {}".format(randnum))

# Introduction
print("Welcome to Guess My Number!. "
      "\nPlease enter a number between 1 and 100."
      "\nWhen you guess too high the computer will tell you high."
      "\nWhen you guess too low the computer will tell you low."
      "\nGuess the number to win!")

# Game Loop
while playerWin is False:
    count += 1
    playerGuess = int(input("Please enter a guess: "))

    if playerGuess is randnum:
        print("\nYou Win with {} guesses!".format(count))
        playerWin = True
    elif playerGuess > randnum:
        print("\nGuess is too High!")
    elif playerGuess < randnum:
        print("\nGuess is too Low!")



# End of Game Loop