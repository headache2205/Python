#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input("Enter the number of elements:"))
numbers=[]
for i in range(n):
    value=int(input("Enter an integer:"))
    numbers.append(value)
result=[]
for value in numbers:
    if value>100:
        result.append("over")
    else:
        result.append(value)
print("Original list:",numbers)
print("Modified list:",result)


# In[6]:


list1=[10,20,30,40]
list2=[40,15,25,20]
print("List1:",list1)
print("List2:",list2)
if len(list1)==len(list2):
    print("The list are of the same length.")
else:
    print("The list have different lengths.")
if sum(list1)==sum(list2):
    print("Both lists sum to the same value.")
else:
    print("The lists sum to different values")
common_values=set(list1)&set(list2)
if common_values:
    print("Yes,these values occur in both lists")
else:
    print("There are no common values between the lists")


# In[7]:


def hello():
    print("Hello world")
hello()


# In[8]:


def hello(name):
    print("Hello",name)
name=input("Enter your name:")
hello(name)


# In[9]:


def calculate(a,b,c):
    print("Sum=",a+b+c)
    print("Product=",a*b*c)
a=int(input("Enter First number:"))
b=int(input("Enter Second number:"))
c=int(input("Enter Third number:"))
calculate(a,b,c)


# In[ ]:




