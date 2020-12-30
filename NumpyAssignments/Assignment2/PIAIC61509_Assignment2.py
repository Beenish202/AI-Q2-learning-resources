#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[4]:


import numpy as np
array=np.arange(0,10)
print("ID array is :",array)
array=array.reshape(2,5)
print("2D Array is :", array)


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[7]:


arr1=np.arange(0,10).reshape(2,5)
arr2=np.ones(10).reshape(2,5)
np.vstack((arr1,arr2))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[8]:


arr1=np.arange(0,10).reshape(2,5)
arr2=np.ones(10).reshape(2,5)
np.hstack((arr1,arr2))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[13]:


arr=np.array([[0,1,2,3,4],[5,6,7,8,9]])
arr.flatten()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[20]:


arr=np.arange(0,15).reshape(1,3,5)
print("DIMENSION:", arr.ndim)
print( "Three Dimension Array is :", arr)
arr2=arr.flatten()
print(" One dimension Array2 is :", arr2)
print("DIMENSION:", arr2.ndim)


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[24]:


arr=np.arange(0,15)
print("One Dimensional Array is", arr)
arr2=arr.reshape(-1,3)
print("Two Dimensional Array is ", arr2)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[25]:


arr=np.arange(25).reshape(5,5)
print(arr)
np.square(arr)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[32]:


np.random.seed(123)
arr=np.random.randint(30,size=(5,6))
print(arr)
np.mean(arr)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[34]:


np.random.seed(123)
arr=np.random.randint(30,size=(5,6))
print(arr)
np.std(arr)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[31]:


np.random.seed(123)
arr=np.random.randint(30,size=(5,6))
print(arr)
np.median(arr)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[33]:


np.random.seed(123)
arr=np.random.randint(30,size=(5,6))
print(arr)
np.transpose(arr)


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[38]:


arr=np.arange(16).reshape(4,4)
print("4 x 4 Matrix is: ",arr)
arr2=np.diagonal(arr)
print("Diagoal Elements: ", arr2)
print("Sum of the Diagonal Elements is: ",sum(arr2))


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[41]:


arr=np.arange(16).reshape(4,4)
print("4 x 4 Matrix is: ",arr)
np.linalg.det(arr)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[42]:


arr=np.arange(10)
print(arr)
print(np.percentile(arr,5))
print(np.percentile(arr,95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[46]:


arr=np.arange(15).reshape(-1,3)
print(arr)
arr_sum=np.sum(arr)
print(arr_sum)
arr_is_nul=np.isnan(arr_sum)
print(arr_is_nul)


# In[ ]:




