import numpy as np

array_s1 = np.arange(10)
print('array : \n', array_s1)

array_s2 = array_s1.reshape(2, 5)
print('array_s2 : \n', array_s2)

array_s3 = array_s2.reshape(5, 2)
print('array_s3 : \n', array_s3)