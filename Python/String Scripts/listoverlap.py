# By Jessica Angela Campisi
# List Overlap
# 10/04/2018
# Description: Compare two lists and return a list that only contains identical members of the first two.
# Exercise 5: https://www.practicepython.org/

# lets get random going
import random
random.seed()

# making a function to return a random number
def giveRandom():
	return random.randrange(1, 20)

# make my lists
a = []
b = []
c = []

# having my lists grab random numbers to fill them. I don't want to make them. sheesh.
count = 10
while count > 0:
	a.append(giveRandom())
	b.append(giveRandom())
	count = count - 1

# print them for all to see.
print("\nList A: {}".format(a))
print("\nList B: {}".format(b))

# test list A against list B
for x in a:
	for y in b:
		if x is y:
			c.append(y)
			
# show the world list C that contains numbers that exist in both a and b.
print("\nBehold! List C! {}".format(c))