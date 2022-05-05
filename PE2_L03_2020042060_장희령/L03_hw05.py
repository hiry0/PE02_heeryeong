# 2020042060 장희령
import numpy as np
a = np.random.randint(1, 100, size = 15).reshape(3, 5)  # 1 to 100, 15 random number generation, (3,5) shape
print(f'a = {a}')

print(f'max of a (axis 0) : {a.max(axis = 0)}') # max along axis 0
print(f'min of a (axis 0) : {a.min(axis = 0)}') # min along axis 0
print(f'mean of a (axis 0) : {a.mean(axis = 0)}')   # mean along axis 0

print(f'max of a (axis 1) : {a.max(axis = 1)}') # max along axis 1
print(f'min of a (axis 1) : {a.min(axis = 1)}') # min along axis 1
print(f'mean of a (axis 1) : {a.mean(axis = 1)}')   # mean along axis 1