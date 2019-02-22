
# coding: utf-8

# In[74]:


#Author: Sorabh Sodhani
#Date: 22nd February, 2019
#Towards: Pirple.com's Python Is Easy
#Project: Project #1 (Connect 4)

#Task: Create the 'Connect 4' Game (a two-player game)
#Useful Link: https://youtu.be/utXzIFEVPjA (Connect 4 Rules)


# In[75]:


# Importing packages

from IPython.display import clear_output
from termcolor import colored, cprint
import numpy as np


# In[76]:


# Defining a matrix to store the game-board status after every move
# Since the game-board consists of 6 Rows and 7 Columns,
# The 'moveMatrix' consists of 6 Rows and 7 Columns as well.

moveMatrix = np.empty((6,7), dtype = "str")
moveMatrix[:] = '.'


# In[77]:


# Defining a function to check if the most recent move by a player is a winning move
# A win happens when any player gets his or her coins in four consecutive cells
# Either horizontally, vertically, or diagonally

def isWinningMove (row, column, playerNumber):

    # Horizontal check:
    # Checking if any three cells to the immediate left and/or right 
    # contain the same color
    
    left = occupancyToTheLeft(row, column, playerNumber)
    right = occupancyToTheRight(row, column, playerNumber)
    horizontalOccupancy = left + right
    if (horizontalOccupancy == 3):
        return True
    
    # Vertical check:
    # Checking if any three cells immediately above and/or below 
    # contain the same color

    verticalOccupancy = occupancyBelow(row, column, playerNumber)
    if (verticalOccupancy == 3):
        return True
    
    # Diagonal Left-Top-to-Right-Bottom check:
    # Checking if any three cells immediately left-above and/or right-below 
    # contain the same color

    lefttop = occupancyAboveLeft(row, column, playerNumber)
    rightbottom = occupancyBelowRight(row, column, playerNumber)
    diagonalOneOccupancy = lefttop + rightbottom
    if (diagonalOneOccupancy == 3):
        return True

    # Diagonal Right-Top-to-Left-Bottom check:
    # Checking if any three cells to immediately right-above and/or left-below 
    # contain the same color
    
    righttop = occupancyAboveRight(row, column, playerNumber)
    leftbottom = occupancyBelowLeft(row, column, playerNumber)
    diagonalTwoOccupancy = righttop + leftbottom
    if (diagonalTwoOccupancy == 3):
        return True

    
    return False


# Function that checks how many adjacent cells to the left
# of the current cell contain the coin of the same color
def occupancyToTheLeft(row, column, playerNumber):
    length = 0
    while (True):
        column -= 1
        if (column >=0 and moveMatrix[row][column] == str(playerNumber)):
            length += 1
        else:
            break
    return length


# Function that checks how many adjacent cells to the right
# of the current cell contain the coin of the same color
def occupancyToTheRight(row, column, playerNumber):
    length = 0
    while (True):
        column += 1
        if (column <= 6 and moveMatrix[row][column] == str(playerNumber)):
            length += 1
        else:
            break
    return length


# Function that checks how many adjacent cells below
# the current cell contain the coin of the same color
def occupancyBelow(row, column, playerNumber):
    length = 0
    while (True):
        row += 1
        if (row <= 5 and moveMatrix[row][column] == str(playerNumber)):
            length += 1
        else:
            break
    return length


# Function that checks how many adjacent cells 
# in the diagonally lower-left direction to
# the current cell contain the coin of the same color
def occupancyBelowLeft(row, column, playerNumber):
    length = 0
    while (True):
        row += 1
        column -= 1
        if (row <=5 and column >=0 and moveMatrix[row][column] == str(playerNumber)):
            length += 1
        else:
            break
    return length


# Function that checks how many adjacent cells 
# in the diagonally upper-right direction to
# the current cell contain the coin of the same color
def occupancyAboveRight(row, column, playerNumber):
    length = 0
    while (True):
        row -= 1
        column += 1
        if (row >= 0 and column <=6 and moveMatrix[row][column] == str(playerNumber)):
            length += 1
        else:
            break
    return length


# Function that checks how many adjacent cells 
# in the diagonally lower-right direction to
# the current cell contain the coin of the same color
def occupancyBelowRight(row, column, playerNumber):
    length = 0
    while (True):
        row += 1
        column += 1
        if (row <= 5 and column <= 6 and moveMatrix[row][column] == str(playerNumber)):
            length += 1
        else:
            break
    return length

# Function that checks how many adjacent cells 
# in the diagonally upper-left direction to
# the current cell contain the coin of the same color
def occupancyAboveLeft(row, column, playerNumber):
    length = 0
    while (True):
        row -= 1
        column -= 1
        if (row >= 0 and column >= 0 and moveMatrix[row][column] == str(playerNumber)):
            length += 1
        else:
            break
    return length


# In[78]:


# Function that records the next move
# and stores it in the moveMatrix
# and also checks if a move is a winning move
# and returns a value accordingly

# Return values:
# 0 if the move was not possible (because a column was full)
# 1 if Player #1 wins with this move
# 2 if Player #2 wins with this move
# 3 if the move was successful but no winner was decided yet

def makeMove(columnNumber, playerNumber):
    spaceAlloted = 0;
    
    # Loop from the top-most row to the bottom-most row (in moveMatrix)
    # of the column chosen by the player so as to find a vacant
    # cell to place the coin in
    
    for i in range(5,-1,-1):
        if(moveMatrix[i][columnNumber-1] == '.'): 
            # Vacant row found!
            
            moveMatrix[i][columnNumber-1] = playerNumber
            # Alloting a cell in moveMatrix to the current player
            
            spaceAlloted = 3 

            drawCurrentBoard(moveMatrix) 

            # Check if this move resulted in a win for the player
            win = isWinningMove(i, columnNumber-1, playerNumber)

            # If a move was a winning move, return the player-number
            if (win):
                return playerNumber
            
            break
    return spaceAlloted  


# In[79]:


# Function that returns the colored unicode 'character' (small circle) for each player
# Player 1's Coin: black circle
# Player 2's Coin: red circle
# Empty Cell: '.' character

def coinAt(value):
    if (value == '1'):
        return colored(u'\u25CF')
    elif (value == '2'):
        return colored(u'\u25CF', "red")
    else:
        return '.'    


# In[80]:


# Defining the function that draws the board with latest moves
# Board has 6 Rows, and 7 Columns

def drawCurrentBoard(moveMatrix):
    clear_output()
    rowCounter, columnCounter = 0, 0

    while (rowCounter < 6):
        print("| ", end = "")

        columnCounter = 0
        while (columnCounter < 7):
            print(coinAt(moveMatrix[rowCounter][columnCounter]), end = "")
            if (columnCounter == 6):
                print(" |")
            else:
                print(" | ", end = "")
                
            columnCounter += 1
            
        print("|-" + "--|-" * 6 + "--|")
        rowCounter += 1

    print("")
    
    for i in range (1,8):
        print("| " + str(i) + " ", end="")

    print("|\n\n")    


# In[81]:


# Initializing the first player
player = 1

# Drawing the starting game-board
drawCurrentBoard(moveMatrix)

moveResult = 0;
while (moveResult == 0 or moveResult == 3):
    chosenColumn = int(input("Player " + str(player) + ", choose a Column Number (0 to Quit): "))
    if (chosenColumn == 0):
        print("Ok. You chose to exit. Take care!")
        break
    elif (chosenColumn > 7):
        print ("Oops! No such column number. Try again?")
        continue
    else:
        moveResult = makeMove(chosenColumn, player)

    if (moveResult == 0):
        print("Ouch! No space left in this column. Try again?")
    elif (moveResult == 3):
        player = ((player + 2)%2) + 1

if (moveResult == 1 or moveResult == 2):        
    print("Voila! Player #" + str(moveResult) + " Wins!\n\nThank You for Playing!")

