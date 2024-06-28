#!/usr/bin/env python
# coding: utf-8

# # Day-5 Python Challenge

# # While Loop

# Write a programe to display the number 1 to 4.

# In[1]:


a = 1
b = 4
while a<=b:
    print(a)
    a = a+1


# Write a programe to enter the value from a user and make a multiplication table till 10.

# In[3]:


x = int(input("Enter Your Number: "))
a = 1
while a<=10:
    print(x*a)
    a = a+1


# In[4]:


count = 0
while (count<5):
    count = count+1
    print("Python")


# # For Loop

# In[7]:


Course = ["Bachelor", "of Computer", "Application"]
for x in Course:
    print(x)


# # Looping though the String

# In[8]:


for x in "Windown":
    print(x)


# In[9]:


for x in range(5): ## They start from 0 to number of value because they print on n-1
    print(x)


# In[10]:


for x in range(2, 5):
    print(x)

