# By Jessica Angela Campisi
# 11/14/2018
# Parse Usernames from PC names
# The username exists as the last 7 characters in a computer name. This script will grab them.

# import only three functions
from random import randrange as rage, seed, choice
from string import ascii_uppercase as upper

seed()


# Generating random computer names
numPcs = 12  # Allows the list of computer names to be dynamic in size.
models = ['L'] * numPcs  # model will always start with L
depts = ['AL', 'BE', 'CN']  # Departments will always have 2 characters
setDepts = [''] * numPcs
initials = [''] * numPcs
idnum = [''] * numPcs
pcname = [''] * numPcs
usernames = [''] * numPcs


# generate random models
for x in range(3):
    for y in range(numPcs):
        models[y] += str((rage(9)))
# generate a random department code
for x in range(numPcs):
    for y in range(2):
        setDepts[x] += choice(upper)

# generate random initials
for x in range(numPcs):
    for y in range(3):
        initials[x] += choice(upper)

# generate a user ID with 4 numbers
for x in range(numPcs):
    for y in range(4):
        idnum[x] += str((rage(9)))

# put it all together now
for x in range(numPcs):
    pcname[x] = models[x] + '-' + setDepts[x] + '-' + initials[x] + idnum[x]

# now to take it apart. I only want the last 7 characters.
for x in range(numPcs):
    usernames[x] = pcname[x][-7:]
    print("PC Name: " + pcname[x] + " Username: " + usernames[x])