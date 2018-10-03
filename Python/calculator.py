# By Jessica Angela Campisi
# Calculator
# 10/2/2018
# Description: A simple calculator. Using Functions, If/Else, int conversion

# define functions
# addition

import sys

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
choice = int(sys.argv[0])

# choice = int(input("Enter choice: "))
print("Enter choice: 1")

# num1 = int(input("What is the first number: "))
# num2 = int(input("What is the second number: "))

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

if choice == 1:
    print("\nTotal: {}".format(add(num1, num2)))
elif choice == 2:
    print("\nTotal: {}".format(subtract(num1, num2)))
elif choice == 3:
    print("\nTotal: {}".format(multiply(num1, num2)))
elif choice == 4:
    print("\nTotal: {}".format(divide(num1, num2)))
elif choice == 5:
    print("\nRemainder: {}".format(mod(num1, num2)))
else:
    print("\nIncorrect entry")