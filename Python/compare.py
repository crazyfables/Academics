# By jessica Angela Campisi
# 11/30/2018
# Code Wars Challenge
# Are they the "same"? Kata

def comp(array1, array2):
    for x in array1:
        if x in array2:
            return True
    return False


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
num =0

for x in a1:
    print("Is {} in a2: ".format(x) + str(comp(a1, a2)))
    print("a2: {0} vs a1: {1}\n".format(a2[num], x))
    if (num != len(a2)):
        num += 1
