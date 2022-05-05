# 2020042060 장희령
import numpy as np
a = np.arange(0, 16).reshape(4, 4) # 0 to 15, (4,4) shape
print(f'b = {a[:, 1]}') # all elements in the second column
print(f'c = {a[2, 1:]}')    # third row, slicing 1 to the end
print(f'd = {a[:2, :2]}')   # 2 by 2 array (slicing 0 to 1)
print(f'e = {a[1:3, 1:3]}') # 2 by 2 array (slicing 1 to 2)