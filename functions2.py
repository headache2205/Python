#!/usr/bin/env python
# coding: utf-8

# In[2]:


def fun(a):
    print(a)
message=input("Enter the Message:")
fun(message)


# In[4]:


numbers=[-5,10,-3,7,0,12,-8]
positive=[x for x in numbers if x>0]
print("Positive numbers:",positive)


# In[6]:


n=int(input("Enter n: "))
numbers=[int(input("Enter a number:"))for i in range(n)]
squares=[x**2 for x in numbers]
print("Squares:",squares)


# In[8]:


word=input("Enter a word:")
vowels=[ch for ch in word if ch.lower() in 'aeiou']
print("Vowels:",vowels)


# In[ ]:




