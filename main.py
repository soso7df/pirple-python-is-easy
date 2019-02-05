
# coding: utf-8

# In[ ]:


#Author: Sorabh Sodhani
#Date: 4th February, 2019
#Towards: Pirple.com's Python Is Easy
#Project: Homework #4 (Lists)

#Task: Lists, Funtions used for Adding to and Removing from Lists


# In[ ]:


# Creating two empty lists - both global

myUniqueList = []
myLeftovers = []


# In[ ]:


# Checking contents of both the lists when initialised

print("Unique List, when initialised: ", myUniqueList) 
print("Leftovers List, when initialised: ", myLeftovers) 


# In[ ]:


# Defining the function that adds only unique values to the myUniqueList

def addToList(newItem):
    #check if this newItem already exists in myUniqueList
    if newItem in myUniqueList:
        #if newItem does exist in myUniqueList, add it to the myLeftovers list and return False
        addToLeftovers(newItem)
        return False
    else:
        myUniqueList.append(newItem)
        return True


# In[ ]:


# Defining the function that adds items to the myLeftovers list

def addToLeftovers(someItem):
    myLeftovers.append(someItem)


# In[ ]:


# Adding unique values to myUniqueList 

addToList('a')
addToList('b')
addToList(1)
addToList(2)


# In[ ]:


# Printing both the lists after addition of unique values

print("Unique List, after adding a few unique values: ", myUniqueList)
print("Leftovers List, after adding a few unique values: ", myLeftovers)


# In[ ]:


# Adding non-unique values to myUniqueList

addToList('a')
addToList(1)


# In[ ]:


# Again, printing both the lists - this time after trying to add non-unique values

print("Unique List, after attempting to add a few non-unique values: ", myUniqueList)
print("Leftovers List, after attempting to add a few non-unique values: ", myLeftovers)

