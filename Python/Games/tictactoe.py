# By Jessica Angela Campisi
# 8/8/2019

# Create the board
# Human Player function

# The Human Player will use Xs
# 1. Show the board. ( Create function, use Board matrix )
def playerTurn(board):
    displayBoard(board)
    print("Where do you want to place your X?")
    choice = int(input("Choice:"))
    if checkPlace(board, choice):




# 2. Ask where they want to place ( Create Choice Variable, Unique to player, no function needed)
# 3. Check to see if that place is taken or not ( create function, create bool)
# 4. Place x in board spot chosen

# Computer Player function
#The computer player will use Os.
# 1. Dumb AI: Random board locations.
#    a. Use random to select spot on matrix.

def translate(a):
    if a is 1:
        return [0, 0]

# 3. Check to see if that place is taken or not ( use function, use bool)
def checkPlace(board, a):
    p = translate(a)
    x = p[0]
    y = p[1]

    if board[x][y] is " ":
        return False
    else:
        return True

# 4. Place o in board spot chosen

# Instructions
"""
Introduce the game
"""

# checkWin
# Check if X or O is 3 across
# top row
def checkWin(board):
    if board[0][0] is board[0][1]  and board[0][0] is board[0][2]:
        return True

# middle row
    if board[1][0] is "X" and board[1][1] is "X" and board[1][2] is "X":
        return True

# bottom row
    if board[2][0] is "X" and board[2][1] is "X" and board[2][2] is "X":
        return True

# left column
# middle column
# bottom column
# back slash
# forward slash


# checkTaken
"""
return true if matrix[x][x] is not " " 
"""

# print board
"""
print board
"""
def displayBoard(board):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in board]))

# Game Loop
def main():
    # Create Variables
    board = [[" ", " ", " "],
             [" ", "X", " "],
             [" ", " ", " "]]
    winner = ""

    while True:
        displayBoard(board)
        playerTurn()
        if checkWin():
            winner = "Player"
            break
        #computerTurn()

"""
print Instructions
loop
    print Board
    player turn
    check win
    computer turn
    check win

print congrats to winner (need winner var) 
"""
main()