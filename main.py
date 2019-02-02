#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Author: Sorabh Sodhani
#Date: 2nd February, 2019
#Towards: Pirple.com's Python Is Easy
#Project: Homework #3 (If Statements)

#Task: Use If Statements in a Function To Produce An Output


# In[16]:


#Defining the Function

def anyEquals(a,b,c):
    if (int(a)==int(b)) or (int(b)==int(c)) or (int(c)==int(a)):
        return True #if any two values are equal (string or integer), return True else return False
    else:
        return False


# In[18]:


print(anyEquals(6,5,"5"))

