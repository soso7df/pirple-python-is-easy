
# coding: utf-8

# In[ ]:


#Author: Sorabh Sodhani
#Date: 7th February, 2019
#Towards: Pirple.com's Python Is Easy
#Project: Homework #6 (Advanced Loops)

#Task: Use functions and loops to print a grid-board with a required number of rows and columns


# In[ ]:


## Setting two global variables 
# for the maximum width and maximum height that my terminal can take 
# This was achieved by trial and error
    
max_rows, max_columns = 22, 22


# In[ ]:


# Defining the function which takes two inputs - rows, and columns
# and draws a grid-like board with as many rows and columns as requested

def drawBoard(rows, columns):
    # If either the requested number of rows and columns is greater than the allowed number
    # then return False
    
    if (rows > max_rows) or (columns > max_columns):
        return False
    
    
    for r in range (1, 2*rows):

        if( r%2 == 0):
            horizontal_separator = "-" + "--+--" * (columns-1) + "-"
            print (horizontal_separator)

        else:
            vertical_separator = " " + "  |  " * (columns - 1) + " "
            print (vertical_separator)

    return True


# In[ ]:


# Calling the function to draw the board

rows, columns = 5, 7
if (drawBoard(rows,columns) == False):
    print ("Oops! Either number of rows or number of columns exceeds the limits set as below")
    print ("Maximum rows: ", max_rows)
    print ("Maximum columns: ", max_columns)

