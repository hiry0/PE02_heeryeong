import numpy as np

array1 = np.arange(start=1, stop=10)

array2 = array1[:3]
print(array2)
print(type(array2))

array2d = array1.reshape(3,3)
print(array2d)
print('row : 0~1, col : 0~1 까지의 값 : \n', array2d[0:2, 0:2])
print('row : 1~2, col : 0~3 까지의 값 : \n', array2d[1:3, :])
print('row : 0~1, col : 0 까지의 값 : \n', array2d[:2, 0])