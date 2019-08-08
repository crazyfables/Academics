# By Jessica Angela Campisi
# 8/8/2019
# Sandbox script

from time import sleep

def makeitmoney(num):
    return '${:,.02f}'.format(num)

def funtext():
    for i in range(1, 20):
        print('-'*i)
        sleep(1)

def menu():
    choice = 99
    while choice is not 0:
        print("Select an item from the menu: ")
        choice = int(input("1. Fun Text"
                           "\n2. Make it Money"
                           "\n3. No Money!"
                           "\n4. Mah List"
                           "\n0. Quit!"
                           "\nChoice: "))
        if choice is 1:
            funtext()
        elif choice is 2:
            number = float(input("Please enter a number: "))
            print(makeitmoney(number))
        elif choice is 3:
            noMath()
        elif choice is 4:
            mahList()
        elif choice is 0:
            print("You quit!")
        else:
            print("Wrong choice!")
        print('-'*40)


def mahList():
    fo = ['Ni', 'SPAM']
    shizzle = ['a', 3, fo]

    print("Printing contents of fo string: {}".format(fo))
    print("Printing contents of shizzle string: {}".format(shizzle))

    shizzle.pop(0)
    print("Removing the first item from shizzle: {}".format(shizzle))

    shizzle.append("Blue")
    fo.append("Yellow")
    print("Adding a value to fo and shizzle: {}".format(shizzle))


def noMath():
    num = float(input("Please enter a number: "))

    print("Turning the number into money")
    num = str(makeitmoney(num))
    print("Result: {}".format(num))

    print("\nRemoving $ from the number")
    num = num.replace('$', '')
    print("Result: {}".format(num))

    print("Removing commas from {}".format(num))
    num = num.replace(',', '')
    num = num.replace('.', '')
    print("Result: {}".format(num))
menu()