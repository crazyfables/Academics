"""
Pig Dice
By Jessica Angela Campisi
Date: 8/7/2019

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


class Pigdice:
    name = ""
    turn = 0
    playerScore = 0
    computerScore = 0
    turnScore = 0

    # Player Turn function
    # roll
    # print results
    # if roll is not one then add to turn score
    # ask player if they want to roll again
    def playerTurn(self):
        roll = self.diceRoll(1, 7) # creates a random number 1-6

        if roll is not 1:
            self.turnScore += roll
            print("\nThe Player rolled a {0}! Their turn score is now {1}!".format(roll, self.turnScore))

            # ask if the player wants to roll again if the score is less than 100
            if self.playerScore + self.turnScore < 100:
                again = input("Roll again? Y/N: ")

                if again.lower() == 'y':
                    self.playerTurn()
                else:
                    print("Player has ended their turn!")
                    self.playerScore += self.turnScore
                    print("The Player's score is now: {}".format(self.playerScore))
            else:
                self.playerScore += self.turnScore
                print("The Player's score is now: {}".format(self.playerScore))

        # if roll is 1 then clear turnScore and tell the player the results
        else:
            self.turnScore = 0
            print("The Player has rolled a 1 and have lost all their points for the turn!")
            print("Their score is sitting at {}".format(self.playerScore))
            time.sleep(3)


    # Roll function
    # pass parameters low, and high
    # return random number between low and high
    def diceRoll(self, low, high):
        return random.randrange(low, high)

    # Computer Turn Function
    # roll
    # print results
    # if roll is not one then add to turn score
    # if turn score is less than 15 then roll again
    def computerTurn(self):
        roll = self.diceRoll(1, 7)
        self.turnScore += roll
        if roll is not 1:
            if self.computerScore + self.turnScore < 100:
                if self.turnScore < 15:
                    print("\nThe Computer Player has rolled a {0}! "
                          "Their turn score is now {1}!".format(roll, self.turnScore))
                    print("The Computer Player decides to roll again!")
                    time.sleep(2)
                    self.computerTurn()
                else:
                    print("The Computer Player has rolled a {0}! "
                          "Their turn score is now {1}!".format(roll, self.turnScore))
                    self.computerScore += self.turnScore
                    print("\nThe Computer Player has decided not to roll again. Their new total is {}".format(
                        self.computerScore))
            else:
                print("\nThe Computer Player has rolled a {0}! "
                      "Their turn score is now {1}!".format(roll, self.turnScore))
                print("The Computer Player's score is now: {}".format(self.computerScore))

        else:
            self.turnScore = 0
            print("The Computer Player has rolled a 1 and have lost all their points for the turn!")
            print("Their score is sitting at {}".format(self.computerScore))
            time.sleep(3)


    # Main Loop
    # Call Roll function with a 0 or 1
    # If turn == 0 then its the player turn
    # if turn == 1 then is the programmer
    # Display turn results
    # if 0 then run player turn function
    # if roll is 1 then turnScore = 0
    # display end of turn score
    # if 1 then run computer turn function
    # if roll is 1 then turnScore = 0
    # display end of turn score
    def mainLoop(self):
        turn = self.diceRoll(0, 2)

        while True:
            if turn:
                print("It's the Player's Turn!")
                self.playerTurn()
                if self.playerScore >= 100:
                    print("\nThe Player Wins!")
                    break
                turn = 0
                self.turnScore = 0
                print("----------------------------------")
            else:
                print("It's the Computer Player's Turn!")
                self.computerTurn()
                if self.computerScore >= 100:
                    print("\nThe computer wins!")
                    break
                turn = 1
                self.turnScore = 0
                print("----------------------------------")


game = Pigdice()
game.mainLoop()