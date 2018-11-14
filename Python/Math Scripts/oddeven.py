# By Jessica Angela Campisi
# Guess My Number
# 10/03/2018
# Description: A random number is generated and the computer will tell the user if it is odd or even
# Exercise 2: https://www.practicepython.org/

import random
random.seed()

number = random.randrange(1, 100)

print("\nGuessing if a number is odd or even...")

if number % 2:
    print("{} is odd! So odd...".format(number))
else:
    print("{} is even, Steven!".format(number))
