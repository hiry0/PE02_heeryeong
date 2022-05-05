# 2020042060 장희령
import numpy as np
c = np.array(range(0, 9))   # array of numbers from 0 to 8

print (c.ndim)   # number of c dimensions
print (c.shape)  # tuple of c dimensions
print (c.size)   # number of elements is the c
print (c.dtype)  # data-type of the c's elements
print (c.itemsize)   # length of one array element in bytes
print (c.data)   # python buffer object pointing to the start of array's data