"""
By Jessica Angela Campisi
Date: 8/6/2019

Create a string, break the string into a list, ask for something to search for, search for that value in the list,
count times that search was found, save where it was found into a new list, print the count and the new new list.

"""

# Create a paragraph python string.
para = "There once was a beetle named Ringo. He wasn't the most popular of the beetles, " \
       "but he was fairly popular. The years had passed and Ringo was now getting old. " \
       "But old age did not stop him from rocking! The band never played on, but Ringo " \
       "certainly did!"

# Ask for character(s) to search the string for.
search = input("What character(s) do you want to search for: ")
count = 0

# parse through the string and find every time the search was found true.
parab = para.split()
results = []

# Search for the search term regardless of upper or lower case. Increment count if found and add item to results string
for i in range(len(parab)):
    if search in parab[i].lower():
        results += parab[i] + " "
        count += 1

# Tell the user
results = "".join(results) # joining to remove useless spacing.
print("Your search yielded {} results!".format(count))
print("Results were found in these words: {}".format(results))
