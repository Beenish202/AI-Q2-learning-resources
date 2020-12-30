#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[6]:


import numpy as np


# 2. Create a null vector of size 10 

# In[7]:


x = np.zeros((10))


# 3. Create a vector with values ranging from 10 to 49

# In[8]:


Rang=np.arange(10, 49)


# 4. Find the shape of previous array in question 3

# In[4]:


Rang.shape


# 5. Print the type of the previous array in question 3

# In[5]:


Rang.dtype


# 6. Print the numpy version and the configuration
# 

# In[9]:


print(np.version)
print(np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[10]:


print(Rang.ndim)


# 8. Create a boolean array with all the True values

# In[11]:


bool_arr=np.ones(10, dtype=bool)
print(bool_arr)


# 9. Create a two dimensional array
# 
# 
# 

# In[12]:


TwoDimArry = np.arange(20).reshape(4,5)
print(TwoDimArry)


# 10. Create a three dimensional array
# 
# 

# In[13]:


ThreeDimArry=np.arange(20).reshape(2,2,5)
print(ThreeDimArry)


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[14]:


OrgArry = np.arange(1, 8)
print("Original array:")
print(OrgArry)
print("Reverse array:")
OrgArry = OrgArry[::-1]
print(OrgArry)


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[15]:


NVct=np.zeros(10)
print(" Null vector of size 10 is : ",NVct)
NVct[5]=1
print ("Null Vector with Fifth value one: ", NVct)


# 13. Create a 3x3 identity matrix

# In[16]:


IdMatx=np.identity(3)
print("3 x 3 2D Identity Matrix is :")
print(IdMatx)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[17]:


arr=np.array([1,2,3,4,5])
#data type of arr before changing the data type
print(f'Before changing : {arr.dtype}')
arr = arr.astype(np.float64)
#data type of arr after changing the data type
print(f'After changing : {arr.dtype}')


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[19]:


import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])  
#print(arr1.transpose())
arr2 = np.array([[0, 4, 1], [7, 2, 12]])
#print(arr2.ndim)
arr1 * arr2


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[24]:


arr1 = np.array([[1., 2., 3.],[4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.],[7., 2., 12.]])
CompArry = arr1 == arr2
#print("Third Array", CompArry)
Reslt = CompArry. all()
print(Reslt)


# 17. Extract all odd numbers from arr with values(0-9)

# In[25]:


arr=np.arange(0,9)
arr[arr % 2 != 0]


# 18. Replace all odd numbers to -1 from previous array

# In[28]:


arr[arr%2!=0]=-1
print(arr)


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[29]:


arr = np.arange(10)
arr[[5,6,7,8]] = 12
print(arr)


# 20. Create a 2d array with 1 on the border and 0 inside

# In[30]:


TwoDArry = np.ones((4,4))
TwoDArry[1:-1,1:-1] = 0
print(TwoDArry)


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[31]:


arr2d = np.array([[1, 2, 3],
                  [4, 5, 6], 
                  [7, 8, 9]])
arr2d = np.where(arr2d == 5,12,arr2d)
print(arr2d)


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[32]:


arr3d = np.array([
    [
        [1, 2, 3], 
        [4, 5, 6]
    ], 
    [
        [7, 8, 9], 
        [10, 11, 12]
    ]
])
arr3d[0][0] = 64
print(arr3d)


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[33]:


arr2d = np.arange(0,10).reshape((2,5))
print(arr2d)
arr2d[0]


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[34]:


arr2d = np.arange(0,10).reshape((2,5))
print(arr2d)
arr2d[1][1]


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[35]:



arr2d = np.arange(0,10).reshape((2,5))
print(arr2d)
arr2d[:,2]


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[38]:


rand = np.random.randn((100)).reshape((10,10))
print(f"Minimun Value {np.amin(rand)}")
print(f"Maximum Value {np.amax(rand)}")


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[44]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(f"Common Elements are : {np.intersect1d(a,b)}")


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[45]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a==b)


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[68]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
print(data)
#mask = (names !='Will')
print("===============================")
print(data[(names !='Will')])


# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[66]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 

data = np.random.randn(7, 4)
print(data)
print('==================================================')
#mask = (names != 'Will') & (names!= 'Joe')
print(data[(names != 'Will') & (names!= 'Joe')])


# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[53]:


rand_arr = np.random.uniform(1,15, size=(5,3))
print(rand_arr)


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[54]:


rand_arr2 = np.random.uniform(1,16, size=(2,2,4))
print(rand_arr2)


# 33. Swap axes of the array you created in Question 32

# In[55]:


print("Original Array")
print(rand_arr2)
print("Swapped Axes")
print(np.swapaxes(rand_arr2, 2, 0))


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[56]:


arr = np.random.uniform(0,20, size=(10))
arr = arr.astype('int32') 
arr =np.sqrt(arr)
arr = np.where(arr < 0.5, 0, arr)
arr = arr.astype('int32')
print(arr)


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[57]:


arr = np.random.uniform(0,20, size=(10))
arr1 = np.random.uniform(0,20, size=(10))
newArr = np.maximum(arr,arr1)
print(f"Array 1 : {arr}")
print(f"Array 2 : {arr1}")
print(f"New Array : {newArr}")


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[58]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.sort(np.unique(names)))


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[59]:


a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
c = np.setdiff1d(a, b)
print(c)


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[60]:


sampleArray = np.array([
    [34,43,73],
    [82,22,12],
    [53,94,66]
])
newColumn = np.array([[10,10,10]])
sampleArray = np.delete(sampleArray, 2, axis=1)
sampleArray = np.insert(sampleArray, 2, newColumn, axis=1)
print(sampleArray)


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[61]:


x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(np.dot(x,y))


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[62]:


arr = np.random.uniform(1,20,size=(4,5))
arr = arr.astype('int32')
print(arr.cumsum())


# In[ ]:




