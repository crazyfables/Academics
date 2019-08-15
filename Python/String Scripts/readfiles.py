# read from files
f = open('data.txt') # open the file
text = f.read() # read data from file
print(text) # print that data

for line in open('data.txt'): print(line)
