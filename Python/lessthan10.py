# By Jessica Angela Campisi
# Guess My Number
# 10/03/2018
# Description: Given a list of numbers, tell the user which ones are less than 10
# Exercise 3: https://www.practicepython.org/

import random
random.seed()

# function to generate and return a random number for the list
def randomNumber():
    return random.randrange(1, 20)


numberList = []
lessThanTen = []
count = 10

# while loop to create a random list of numbers
while count > 0:
    numberList.append((randomNumber()))
    count = count - 1

# test if each number is less than 10 then add them to lessThanTen list
for x in numberList:
    if x < 10:
        lessThanTen.append((x))

# we have to tell the user something! Can't leave them in the dark. Why you so cruel??
print("\nThe computer is generating a list of numbers less than 10!")
print("\n\nNumbers: {}".format(numberList))
print("\nNumbers less than 10: {}".format(lessThanTen))
print("\nJust wanna point out... you're not gonna see 10, cause... less than 10, ya know.")