import numpy as np

array_8 = np.arange(8)
array3d = array_8.reshape(2, 2, 2)
print('array3d :', array3d.tolist())

array5 = array3d.reshape(-1, 1)
print('array5 :', array5.tolist())
print('array5 shape :', array5.shape)

array6 = array_8.reshape(-1, 1)
print('array6 :', array6.tolist())
print('array6 shape :', array6.shape)