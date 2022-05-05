import numpy as np

array_int = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(type(array_int))
print(array_int.dtype)
print(array_int.ndim)
print(array_int.shape)

array_float = array_int.astype('float')
print(array_float)
print(array_float.dtype)