
# coding: utf-8

# In[ ]:


#Author: Sorabh Sodhani
#Date: 2nd February, 2019
#Towards: Pirple.com's Python Is Easy
#Project: Homework #3 (If)

#Task: Use "If" statements


# In[ ]:


# Defining the Comparison Function

def anyEquals(value1, value2, value3):
    # If any two values are equal, return True, else return False
    # The values can be anything - integers, floats, strings too
    if ( (int(value1) == int(value2)) or (int(value2) == int(value3)) or (int(value3) == int(value1)) ):
        return True
    else:
        return False


# In[ ]:


# Calling the function with a few combinations
# Combination 1: 5, 4, 6

a, b, c = 5, 4, 6

if (anyEquals(a,b,c)):
    print("Values being compared (" , a,b,c, ") have equals")
else:
    print("Values being compared (" , a,b,c, ") DO NOT have equals")


# In[ ]:


# Calling the function with a few combinations
# Combination 2: 5, 4, 5

a, b, c = 5, 4, 5

if (anyEquals(a,b,c)):
    print("Values being compared (" , a,b,c, ") have equals")
else:
    print("Values being compared (" , a,b,c, ") DO NOT have equals")


# In[ ]:


# Calling the function with a few combinations
# Combination 3: 6, 5, "5"

a, b, c = 6, 5, "5"

if (anyEquals(a,b,c)):
    print("Values being compared (" , a,b,c, ") have equals")
else:
    print("Values being compared (" , a,b,c, ") DO NOT have equals")

