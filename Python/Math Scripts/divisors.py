# By Jessica Angela Campisi
# Guess My Number
# 10/04/2018
# Description: Request a number from the user and find every number that divides evenly.
# Exercise 4: https://www.practicepython.org/

# Instruct User
print("Divisor Program "
      "\nYou will enter a number and see all possible divisors.\n")

# Request Input
num = int(input("Please enter a number: "))
numRange = range(1, num)
numList = []

# Loop to iterate through numbers till 2.
for elem in numRange:
    # if num % elem equals 0 then add the current element to the list
    if num % elem is 0:
        numList.append(elem)

# print the results
print("\nEntire list of good divisors for {0}: ".format(num))
print(numList)

