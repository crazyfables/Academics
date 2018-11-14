# By Jessica Angela Campisi
# Super List
# 10/05/2018
# Description: A playground for lists.

# make an empty list
my_list = []

# print empty list, that's how we do.
print(my_list)

# change value and make another list
my_list = ["Bill", "Cypher", "Damon", "Jack Frost"]
other_list = ["Dawn", "Fredo", "Hall 9000", "Goku"]

# print both
print("\nMy List: {}".format(my_list))
print("\nMy other list: {}".format(other_list))

# time to show list functions

# erase the list. We don't talk to those people.
print("\nClearing my_list")
my_list.clear()

print("\nAdding Jessica to my_list")
# add a name to it again.
my_list.append("Jessica")

# print to see content
print("\nMy List again: {}".format(my_list))

# lets do a copy of one list to another
my_list = other_list.copy()

# adding Jessica again
my_list.append("Jessica")

# print list again
print("\nMy list again again: {}".format(my_list))

# time to count off
print("Size of my_list: {}".format(len(my_list)))
print("Size of other_list: {}".format(len(other_list)))


#my_list.extend()
#my_list.index()
#my_list.insert()
#my_list.pop()
#my_list.remove()
#my_list.reverse()
#my_list.sort()