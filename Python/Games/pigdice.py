"""
Decide who will start by having each player roll a dice – the one with the highest score starts the game
A player’s turn starts by rolling only one dice. The player continues to roll the dice again, as long as he does not
roll a 1 or decides to add his points to his overall score. Each time the player rolls the dice, the following options
exist:

The player rolls a 1 – his turn ends without any points (he also loses the points from any previous rolls in the current
 turn).

Any other number than a 1 is rolled – the player can add that number to the points scored in his current turn and
continue by rolling the dice again.

The player decides to end his current turn and add all the points from his turn to his overall score.

The game ends when a player has reached 100 points and becomes the winner of the game!

"""
import random, time

random.seed()

# function rolls the dice getting a number between 1 and 6 and return that value to the main loop
def diceRoll(player):
    random.seed()
    # print("Rolling the dice...")
    diceroll = random.randrange(1, 7)
    if player == 0:
        player = "Player"
    else:
        player = "Computer Player"
    print("{0} rolled a {1}!".format(player, diceroll))
    time.sleep(1)
    return diceroll


playerTurn = random.randrange(0, 2)
playerScore = 0
computerScore = 0
roll = 0
winner = ""

# if 0 the player will go first, else the computer will
if playerTurn:
    print("Player will go first!")
else:
    print("Computer Player will go first!")

while playerScore < 100 and computerScore < 100:

    # start the player turn
    if playerTurn == 0:
        print("\nThe Player will now go.")

        while roll is not 1 and playerScore < 100:
            # roll dice
            roll = diceRoll(playerTurn)
            playerScore += roll

        # display player score, pause before next player turn, and reset token values
        print("Final Score for the turn is: {}".format(playerScore))
        time.sleep(2)
        playerTurn = 1
        roll = 0

    else:
        print("\nThe Computer Player will now go.")

        while roll is not 1 and computerScore < 100:
            # roll dice
            roll = diceRoll(playerTurn)
            computerScore += roll

        # display computer score, pause before next player turn, and reset token values
        print("Final Score for the turn is: {}".format(computerScore))
        time.sleep(2)
        playerTurn = 0
        roll = 0

print("And the final winner is: {}!".format(winner))