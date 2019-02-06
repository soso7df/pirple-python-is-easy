
# coding: utf-8

# In[ ]:


#Author: Sorabh Sodhani
#Date: 6th February, 2019
#Towards: Pirple.com's Python Is Easy
#Project: Homework #5 (Loops)

#Task: Use Loops to print words "Fizz" and "Buzz" for numbers between 1 and 100 divisible by 3 and 5 respectively along with an added functionality of printing "Prime" for prime numbers


# In[ ]:


# Important: Confusion (and Assumption Made)

# What should be done for the special case of 3 and 5?
# Because while they should make me print Fizz and Buzz respectively
# But both numbers are also prime themselves

# So I am printing both Fizz and Prime for 3
# And Buzz and Prime for 5

# Also assuming that 1 is a prime number


# In[ ]:


# Defining a function to deduct if a given number is a prime number or not

def isPrime(N):
    for n in range(2, N): # because we need a range from 2 to (N - 1) 
        if (N % n == 0):  # N is divisible by at least 1 number between 2 and (N-1)
            return False  # return False if not a prime

    return True


# In[ ]:


num1, num2 = 3, 5 #using variables to generalise the code

# Loop through all numbers from 1 to 100
for n in range(1,101):
    
    # Initialise a string that we will eventually print
    toPrint = ""
    
    # Check if current number is divisible by  3
    if (n % num1 == 0):
        toPrint = "Fizz"
    
    # Check if current number is divisible by 5
    if (n % num2 == 0):
        toPrint += "Buzz"
        
    # So, if the current number is divisible by both 3 and 5
    # toPrint will contain "FizzBuzz"
       
    # Check if current number is a prime
    if (isPrime(n)):
        toPrint += "Prime"
        
    # Print the number, and the results from the three checks above
    print(n, toPrint)

