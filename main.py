
# coding: utf-8

# In[ ]:


# Author: Sorabh Sodhani
# Date: 19th February, 2019
# Towards: Pirple.com's Python Is Easy
# Project: Homework #8 (I/O)

#Task: File Operations


# In[2]:


# Querying user for the file name 

fileName = str(input("Please enter the name of the file on which you want to operate: "))


# In[3]:


# Check is file exists

import os.path
from os import path

fileExists = path.exists(fileName)

if (fileExists):
    print (fileName + " file exists!")
else:
    fileObject = open(fileName, "w")
    print("File " + fileName + " doesn't exist. No worries, a file of the same name is now created.")
    newString = str(input("Please enter the text you want to write to this new file: "))
    fileObject.write(newString)
    fileObject.close()
    exit()


# In[4]:


# Defining various functions for each file operation

# toJustRead for simply reading the file contents
def toJustRead():
    print("Thank you. You chose to simply read the file. The file contents are:\n")
    tempFile = open(fileName)
    for line in tempFile:
        print(line, end = "")

# toDelete for simply deleting the contents of the file        
def toDelete():
    print('Thank you. You chose to delete all contents of the file.')
    tempFile = open(fileName, "w")
    print('All contents of the file have been deleted!')

# toAppend for adding new content to the file
def toAppend():
    print('Thank you. You wish to add a new line to the file.')
    newLine = str(input('Please enter the new content: '))
    tempFile = open(fileName, "a")
    tempFile.write(newLine + "\n")
    print('The new content has been added to the file!')

# toReplace for replacing a specified line with a new line
def toReplace():
    print('Thank you. You wish to replace a specific line with another one.')
    lineNumber = int(input('Which line do you want to replace? '))
    newContent = str(input('Please enter the content that should replace line number ' + str(lineNumber) + ': ' ))
    tempFile = open(fileName, "r+")
    counter = 1;
    newFileContent = ""
    for line in tempFile:
        if (counter == lineNumber):
            newFileContent = newFileContent + newContent + "\n"
        else: 
            newFileContent = newFileContent + line
        counter += 1
    tempFile.close()
    tempFile = open(fileName, "w")
    tempFile.write(newFileContent)
    print("Line number " + str(lineNumber) + " has been replaced!")


# In[5]:


# initializing a {number : function name} dictionary to make it easy 
# to replicate the 'switch' functionality which isn't avilable in Python
# to call the desired funciton without getting into an if-else loop

operations = {
                1 : toJustRead, 
                2 : toDelete, 
                3 : toAppend, 
                4 : toReplace,
                5 : exit
}


# In[6]:


# Presenting choices to the user ...

print("Please enter a number for what you wish to do with the file ...")
print("1: Read the file")
print("2: Delete all contents of the file")
print("3: Append to the existing contents in the file")
print("4: Replace a specific line with a new line")
print("5: Exit!")

# Receiving user's input ...
whatOperation = int(input ("Enter choice: "))

# Calling appropriate function based on user's input ...
operations[whatOperation]()

