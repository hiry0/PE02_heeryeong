# 2020042060 장희령
import numpy as np
a = np.array([[1, 1, -1], [2, -1, 3], [1, 2, 1]])   # coefficient
b = np.array([0, 9, 8]) # constant
x = np.linalg.solve(a,b)    # solution of an equation
print(f' x = {x[0]}, y = {x[1]}, z = {x[2]}')