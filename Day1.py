#!/usr/bin/env python
# coding: utf-8

# In[3]:


# variable
a = 10
b = "Hello"
print(a) 
print(b)


# In[5]:


num = int(input("Enter a number"))
print(num)


# In[10]:


num1 = "256"
print(type(num1))
num1 = int(num1)
print(type(num1))


# In[14]:


a=10
if a>10:
    print("Larger than 10")
elif a==10:
    print("Equal to 10")
else:
    print("smaller than 10")


# In[37]:


#break: Exits the loop entirely, regardless of whether the sequence has been fully iterated.
for i in range(0,5):
    if i==3:
        break
    print(i)


# In[36]:


#continue: Skips the current iteration and moves to the next item in the sequence.
for i in range(0,5):
    if i==2:
        continue
    print(i)


# In[39]:


#pass: Acts as a placeholder when a statement is syntactically required but you don't want any code to execute.
for i in range(0,5):
    pass


# In[40]:


# ELSE BLOCK The code in the else block is executed only if the loop finishes all its iterations naturally (i.e., is not terminated by a break statement). 
for i in range(3):
    print(i)
else:
    print("Loop finished without breaking!")


# In[46]:


a =5;
while a>0:
    print(a)
    a-=1


# In[50]:


# function 
# function defination
def greet(name):
    return f"Hello {name}, You are a Genius"
# calling function and passing parameter
greet("Priyanshu")


# In[51]:


# default argument
def greet(name="Sir"):
    return f"Hello {name}, You are a Genius"
greet()


# In[50]:


# Print “Hello Python”
print("Hello Python")
# Take name input and print greeting

name = str(input("Enter your name"))
print(f"Hello {name}")

# Add two numbers
a=10
b=20
print(a+b)

# Check even/odd
num = int(input("Enter a number"))
if num//2==1:
    print("odd")
else:
    print("even")

# Check positive/negative/zero
num = int(input("Enter an integer"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")

# Find max of 2 numbers
a=10
b=20
if a>b:
    print(f"a is greatest")
else:
    print(f"b is greatest")

# Find max of 3 numbers
a=10
b=40
c=30
if a>b and a>b:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")

# Check leap year
year = int(input("Ener the year"))
if year%4 == 0 :
    print("Leap year")
else:
    print("Not a leap year")

# Print 1 to N
n = int(input("Enter N : "))
for i in range(1,n+1):
    print(i)

# Print N to 1
n = int(input("Enter N : "))
for i in range(n,0,-1):
    print(i)


# Sum of 1 to N
n = int(input("Enter N : "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

# Factorial of N
n = int(input("Enter N : "))
result=1
for i in range(1,n+1):
    result*=i
print(result)

# Count digits in a number
num = int(input("Enter Number : "))
count=0
while num>0:
    num=num//10
    count=count+1
print(count)

# Reverse a number
num = int(input("Enter Number : "))
sign = -1 if num<0 else 1
num = abs(num)
rem=0
rev=0
while num>0:
    rem = num%10
    rev = rev*10+rem
    num//=10
rev*=sign
print(rev)


# Check palindrome number
num = int(input("Enter Number : "))
org = num
sign = -1 if num<0 else 1
num = abs(num)
rem=0
rev=0
while num>0:
    rem = num%10
    rev = rev*10+rem
    num//=10
rev*=sign
if(org == rev):
    print("Palindrome")
else:
    print("Not a palindrome")

# Sum of digits
num = int(input("Enter Number : "))
num = abs(num)
sum=0
while num>0:
    rem = num%10
    sum+=rem
    num//=10
print(sum)

# Armstrong number (basic)
num = int(input("Enter Number : "))
num = abs(num)
power = len(str(num))
n=num
total = 0
while n>0:
    digit = n%10
    total += digit**power
    n//=10
if total==num:
    print("Armstrong number")
else:
    print("Not a armstong number")

# Fibonacci series up to N terms

# Prime check

# Print primes in a range

# Multiplication table of N

# Count vowels in a string

# Reverse a string

# Check palindrome string

# Simple function: is_prime(n) returning True/False





# In[ ]:




