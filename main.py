
# coding: utf-8

# In[ ]:


#Author: Sorabh Sodhani
#Date: 2nd February, 2019
#Towards: Pirple.com's Python Is Easy
#Project: Homework #2 (Functions)

#Task: Assign and Print Variables


# In[ ]:


#Assigning Values to Variables
Title = "La Vie en rose" #the title of the track
Artist = "Louis Armstrong" #the main artist of the song, sometimes also the artist of the entire album
Album = "None (Solo Recording)" #the album to which the song belongs
Genre = "Jazz" #the category of the song
Length = 3.23 #length of the song in minutes.seconds
Track_Number = 1 #position of the song in the album, relative to other songs
Bitrate_Unit = "kbps" #kilobytes per second
Bitrate_Value = "320" #normally a value between 128 and 320, usually higher bitrates mean better sound quality
Recording_Year = 1950 #year in which the song or album was recorded


# In[ ]:


#Defining Functions
def title():
    global Title; #not necessary to define a global variable here but just a safe practice
    return Title; #returns the 'Title'

def artist():
    global Artist; 
    return Artist; #returns the 'Artist'

def length():
    global Length; 
    return Length; #returns the 'Length'


# In[ ]:


#Printing Values of Variables 
print ("Title:" ,title())
print ("Artist:" ,artist())
print ("Length:" ,length(), "m")


# In[ ]:


#Defining a Boolean Return Function
def isLong(): #returns True if the song is longer than 10 minutes, False otherwise
    if (Length > 10):
        return True
    else:
        return False
    
    


# In[ ]:


print("The song is longer than 10 minutes:", isLong())

