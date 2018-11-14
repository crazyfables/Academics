# By Jessica Angela Campisi
# Calculator
# 10/2/2018
# Description: A simple calculator. Using Functions, If/Else, int conversion
# script has been updated to require zero input for travis ci testing.

# define functions
# addition

import random


def add(a: int, b: int):
    return a + b


# subtraction
def subtract(a: int, b: int):
    return a - b


# multiply
def multiply(a: int, b: int):
    return a * b


# divide
def divide(a: int, b: int):
    return a / b


# modulus
def mod(a: int, b: int):
    return a % b


# start random seeds for CI testing removing user entry.
random.seed()
num1 = 0
num2 = 0

# instructions
def instructions():
    print("Do you want to... "
          "\n1....Add"
          "\n2....Subtraction"
          "\n3....Multiply"
          "\n4....Divide"
          "\n5....Modulus")

instructions()
# testing the build
choice = random.randrange(1, 5)

# choice = int(input("Enter choice: "))
print("Enter choice: {}".format(choice))

# num1 = int(input("What is the first number: "))
# num2 = int(input("What is the second number: "))

while num1 <= num2:
    num1 = random.randrange(1, 100)
    num2 = random.randrange(1, 100)

if choice == 1:
    print("\nAddition!")
    print("\n{0} + {1} = {2}".format(num1, num2, add(num1, num2)))
elif choice == 2:
    print("\nSubtraction!")
    print("\n{0} - {1} = {2}".format(num1, num2, subtract(num1, num2)))
elif choice == 3:
    print("\nMultiply!")
    print("\n{0} * {1} = {2}".format(num1, num2, multiply(num1, num2)))
elif choice == 4:
    print("\nDivide!")
    total = (divide(num1, num2))
    total = '%.2f'%total
    print("\n{0} / {1} = {2}".format(num1, num2, total))
elif choice == 5:
    print("Modulus!")
    print("\n{0} % {1} = {2}".format(num1, num2, mod(num1, num2)))
else:
    print("You entered something dumb!")

    print("Incorrect choice...")