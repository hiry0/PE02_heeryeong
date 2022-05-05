import numpy as np

array1 = np.arange(10)
print(array1)
array2 = array1.reshape(-1, 5)
print('array2 shape :', array2.shape)
array3 = array1.reshape(5, -1)
print('araay3 shape :', array3.shape)