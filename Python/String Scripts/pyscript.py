# By Jessica Angela Campisi
# 9/25/2018
# pyscript.py
# Title: Just a Simple Tutorial Part 1
# Description: An introductory python tutorial. This script teaches basic commenting, functions (print), variable
# assignments, TO DOs, and simple string formatting.

# I am a comment. Comments have # preceding them. They can be on their own line or at the end of a line of code.

# Print is a function in python. Functions are given a name and always have parentheses in them ().
# Text surrounded by "" is considered a literal string. As literally everything inside of it is printed to the screen
# as is.
#
# \n is an exception to this. \ acts as an escape character. It allows you to include a new line \n, a quotation
# mark \", a tab \t, and more.

print("\nHello World")

# Variables are containers. In python anything can go in this container and it's fine with it. However, later in your
# code you may run into issues if you keep changing a variable type from string, to integer, to tuple, and more.
# It also makes it confusing to follow along by you or another programmer.
# There are various ways to handle naming a variable. The example given is camel case notation. The first word is
# lowercase. Any new words start with the first letter as an uppercase.
# Another option (and these can be combined) is giving the type at the beginning of the variable. So strCharName.

# Input is a quick way to grab information. However, it only grabs strings, not integers or any other type.
# To make use of this you would need to do a type conversation.
# In this example I am asking the question "What is your name: " Notice I put a space there after the question.
characterName = input("What is your name: ")

# In this example we introduce .format(variableName) after the literal string. {} is a placeholder for information.
# If you end up including 2 or more instances of {} you should use {0}, {1}, {2}, etc... instead. Python will not like
# it even if you use the same variable twice.
print("Please to meet you {}!".format(characterName))

# Won't work.
# print("Please to meet you {}! Your mustache is amazing, {}!".format(characterName))

# Will work
print("Please to meet you {0}! Your mustache is amazing, {0}!".format(characterName))


# Declaring string variables with information already.
characterClass = "crazybarian" # Barbarian and an insane person combined into one!
characterWeapon = "butter knife of doom"

# I am creating a simple story that uses a predefined name, class, and weapon. I've used the variables out of order,
# but called them in the correct sequence I need. The order is almost never important as long as you know how to call
# the right variables at the right time. It is easier to add them in the order of their use.

# I want you to note that I have also broken down the variable assignment into two different lines.
# It's important to minimize how long a line is so that the reader doesn't need to control both the vertical and the
# horizontal.
myStory = "\nThere once was a {1} named {0}. This {1} was very sad. \nTheir only weapon, the {2}, was damaged.".format(
    characterName, characterClass, characterWeapon)
print(myStory)

characterName = input("\n{0} decided to have a name change. What is {0}'s new name: ".format(characterName))
lineBreak = "\n-----------------------------------------------"
# Printing the story again
print(lineBreak)
print(myStory)

# I am combining an existing string variable with some new information that has its own string formatting. This time
# I have interrupted the literal string (text).
myStory = myStory + " {0} walked \nmany miles, about 500 of them to be exact. And now he's at your door." \
                    "\n\"Fix my {1}\", they say.".format(characterName, characterWeapon)

# Printing the story again
print(lineBreak)
print(myStory)
print("\nThe End")

# TO DO comments can work interactively with an editor to allow you to note where you need to work in the future.
# This could be in creating a function/feature or to fix something that you know is having issues.
# Using TO DO proactively will help to define the work needs to be done.

# TODO: Fix breaks

# TODO: Write more code

# TODO: Never give up, never surrender!

# TODO: Go and make your own story driven narrative with the information gained. Make it 3 paragraphs with 4 variables.
