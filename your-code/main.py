#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Import the NUMPY package under the name np.
import numpy as np


# In[3]:


#2. Print the NUMPY version and the configuration.
print(np.__version__)


# In[4]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
#4. Print a.
a=np.random.random((2,3,5))
print("2x3x5 3-dimensional array with random values \n", a)


# In[5]:


a2=np.random.randint(low=0, high=10, size=(2,3,5))
print("2x3x5 3-dimensional array with random values \n", a2)


# In[6]:


a3=np.random.rand(2,3,5)
print("2x3x5 3-dimensional array with random values \n",a3)


# In[7]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
#6. Print b
b=np.ones((5,2,3))
print("5x2x3 3-dimensional array with all values equaling 1: \n",b)


# In[8]:


#7. Do a and b have the same size? How do you prove that in Python code?
print("Are size the same?:",a.size==b.size)


# In[9]:


print("Are shape the same?:",a.shape==b.shape)


# In[10]:


#8. Are you able to add a and b? Why or why not?
print("We aren't able to add a +b because they have differents shapes")


# In[11]:


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array 
#to varialbe "c".
c=b.reshape(2,3,5)
print("b transpose",c)


# In[12]:


print(a.shape)
print(b.shape)
print(c.shape)


# In[13]:


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d=a+c
print("Because both arrays have same shape")
print("a+c",d)


# In[14]:


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("a printed\n",a)
print("d printed\n",d)
print("Each element of d,is each element of a plus 1")


# In[15]:


#12. Multiply a and c. Assign the result to e.
e=np.multiply(a,c)
print("a multiply by c",e)


# In[16]:


#13. Does e equal to a? Why or why not?
print("Does e equal to a?",e==a)
print("Because c is a matrix of ones")


# In[17]:


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max=d.max()
print("max d",d_max)
d_min=d.min()
print("min d",d_min)
d_mean=d.mean()
print("mean d",d_mean)


# In[18]:


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5)
#as d using `np.empty`.
f=np.empty((2,3,5))
print(f)


# In[19]:



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, 
assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i,j,k] > d_mean and d[i,j,k]< d_max:
                f[i,j,k]=75
            if d[i,j,k] == d_mean:
                f[i,j,k]=50
            if d[i,j,k] > d_min and d[i,j,k]< d_mean:
                f[i,j,k]=25
            if d[i,j,k] == d_max:
                f[i,j,k]=100
            if d[i,j,k] == d_min:
                f[i,j,k]=0
  


# In[20]:


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print("This is d")
print(d)
print("\n This is f")
print(f)


# In[30]:


"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
""""""
#En Python las cadenas de texto son arrays con caracteres alfanuméricos,
#por lo que no es necesario disponer de funciones especificas. 
#El tratamiento se pude realizar de la misma manera que cualquier otro tipo de arrays.

""""""
string_array=np.empty(f.shape, dtype=np.str_)


# In[31]:


f.shape


# In[32]:


for i in range(f.shape[0]):
    for j in range(f.shape[1]):
        for k in range(f.shape[2]):
            if f[i,j,k]==0:
                string_array[i,j,k]="A"
            elif f[i,j,k]==25:
                string_array[i,j,k]="B"
            elif f[i,j,k]==50:
                string_array[i,j,k]="C"
            elif f[i,j,k]==75:
                string_array[i,j,k]="D"
            elif f[i,j,k]==100:
                string_array[i,j,k]="E"
print("A,B,C,D,E array") 
print(string_array)                

