
# coding: utf-8

# In[ ]:


# Author: Sorabh Sodhani
# Date: 9th February, 2019
# Towards: Pirple.com's Python Is Easy
# Project: Homework #7 (Variables)

#Task: Dictionaries


# In[ ]:


# Defining the mySong Variable (a dictionary, and global)

mySong = {}


# In[ ]:


# Assigning Keys and Values

mySong["title"] = "La Vie en rose" #the title of the track
mySong["artist"] = "Louis Armstrong" #the main artist of the song, sometimes also the artist of the entire album
mySong["album"] = "None (Solo Recording)" #the album to which the song belongs
mySong["genre"] = "Jazz" #the category of the song
mySong["length"] = "3.23m" #length of the song in minutes.seconds
mySong["track number"] = 1 #position of the song in the album, relative to other songs
mySong["bitrate value"] = "320kbps" #normally a value between 128 and 320, usually higher bitrates mean better sound quality
mySong["recording year"] = 1950 #year in which the song or album was recorded


# In[ ]:


# Printing Values of Variables

for key in mySong:
    printString = key + ": " + str(mySong[key])
    print(printString)
    


# In[ ]:


# Defining the quizzing function

def songQuiz (key, value):
    userInput = str(input("Guess the song's " + key + ": "))
    if (userInput == str(value)):
        return True
    else:
        return False


# In[ ]:


# Calling the quizzing function to ask the question

quizzed_property = "genre" # trial with an existing key
# quizzed_property = "location" # trial with a non-existent key


if (quizzed_property in mySong):
    result = songQuiz(quizzed_property, mySong[quizzed_property])
else:
    print("The property '" + quizzed_property + "' doesn't exist.")


# In[ ]:


# Evaluating the user's input and printing a suitable comment

if (result == True):
    print("Nice! That's correct!")
else:
    print("Oops. You got it wrong!")

