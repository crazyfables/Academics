# By Jessica Angela Campisi
# Prime Finder
# 11/13/2018

# This script is made entirely to print out obnoxiously large numbers and take forever doing so.
num = 251221
total = 2
while total < num ** num:
    total *= total
    print(total)