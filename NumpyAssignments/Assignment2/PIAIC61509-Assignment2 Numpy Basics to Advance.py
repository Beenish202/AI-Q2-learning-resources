#!/usr/bin/env python
# coding: utf-8

# # Task no 1

# In[2]:


import numpy as np


def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x


# In[6]:


X=function1()
print(X)


# # Task no 2

# In[33]:


def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
    x = np.arange(10,37, dtype=np.float64).reshape((3,3,3))     #wrtie your code here
    #Y=  np.arange(10:36,, dtype=np.float64).reshape((3,3,3)) 

    return x


# In[34]:


function2()


# # Task no 3

# In[35]:


def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[(a%5==0) & (a%7==0)] #wrtie your code here
    return x


# In[37]:


reslt=function3()
print(reslt)


# # Task no 4

# In[57]:



def function4():
    #Swap columns 1 and 2 in the array arr.
   
    arr = np.arange(9).reshape(3,3)
    print("original Array :", arr)
    arr[:,[1, 2]] = arr[:,[2, 1]]
    return arr


# In[59]:


Y=function4()
print("Swapped array is :", Y)


# # Task5

# In[60]:


def function5():
    #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
    z = np.zeros(20).reshape(4,5)
  
    return z


# In[62]:


function5()


# # Task6

# In[63]:


def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
    arr =np.zeros(10)
    arr[5]=10
    arr[8]=20
      
    return arr


# In[64]:


function6()


# # Task7

# In[65]:



def function7():
    #  Create an array of zeros with the same shape and type as X. Dont use reshape method
    x = np.arange(4, dtype=np.int64)
    X=np.zeros(4,dtype=np.int64)
    return X


# In[66]:


function7()


# # Task 8

# In[77]:


def function8():
    # Create a new array of 2x5 uints, filled with 6.
    
    x = np.arange(10, dtype=np.uint32).reshape(2,5)
    x[:,:]=6
    
    return x
function8 ()


# # Task 9

# In[82]:


def function9():
    # Create an array of 2, 4, 6, 8, ..., 100.
    a =np.arange(1,102)
    a=a[a%2==0]
  
    return a
function9()


# # Task 10

# In[89]:


def function10():
    # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
    
    arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
    brr = np.array([1,2,3])
    subt = arr-np.vstack(brr) 
  
    return subt
function10()


# # Task 11

# In[106]:


def function11():
    # Replace all odd numbers in arr with -1 without changing arr.
    
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    ans =np.where(arr%2!=0,-1, arr)
    
  
    return ans
function11()


# # Task 12

# In[108]:


def function12():
    # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
    # HINT: use stacking concept
    
    arr = np.array([1,2,3])
    ans = np.hstack((arr.repeat(3),arr,arr,arr))
  
    return ans
function12()


# # Task 13

# In[114]:


def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans = arr[(arr>5) & (arr<10)]
    
    return ans
function13()
#write your code here 


# # Task 14

# In[116]:


def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    
    import numpy as np
    arr = np.arange(10, 34, 1) #write reshape code
    ans = arr.reshape(4,2,3)
  
    return ans
function14()


# # Task 15

# In[119]:


def function15():
    #Sort following NumPy array by the second column
    
    
    arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
    print(arr)
    ans = arr[[1,0,2]]
  
    return ans
function15()


# # Task16

# In[121]:


def function16():
    #Write a NumPy program to join a sequence of arrays along depth.
    
    
    x = np.array([[1], [2], [3]])
    y = np.array([[2], [3], [4]])
    ans = np.hstack([x,y]) 
  
    return ans
function16()


# # Task 17

# In[124]:


def function17():
    # replace numbers with "YES" if it divided by 3 and 5
    # otherwise it will be replaced with "NO"
    # Hint: np.where
    arr = np.arange(1,10*10+1).reshape((10,10))
    ans=np.where((arr%3==0) & (arr%5==0),'Yes','No')
    
    return ans

function17()


# # Task 18

# In[125]:


def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = x = len(np.intersect1d(piaic,students))
    return x
function18()


# # Task 19

# In[126]:


def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:

    X =  np.arange(1,26).reshape(5,5)
    W = X.T  
    b = 5  
    output = (X*W)+b
    return output 
function19()


# # Task 20

# In[130]:


def fucntion20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def xyz(x):
        return x*2+3-2

    return xyz(x)

fucntion20()


# In[ ]:




