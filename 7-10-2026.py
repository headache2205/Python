#!/usr/bin/env python
# coding: utf-8

# In[3]:


def leapyear():
    a=int(input("Enter current year"))
    b=int(input("Enter the last year needed"))
    for i in range(a,b):
        if(i%4==0):
            print(f"{i} is a leap year")
            a=i+4
        else:
            a=a+1
leapyear()


# In[ ]:




