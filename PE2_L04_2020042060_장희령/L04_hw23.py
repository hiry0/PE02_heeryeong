import numpy as np

array1d = np.arange(start=1, stop=10)
array1d[0] = 9
array1d[8] = 0
print(type(array1d[0]))
print(array1d)

array2d = array1d.reshape(3, 3)
print(array2d)

print('(0,0) 값 :', array2d[0,0])
print('(2,2) 값 :', array2d[2,2])