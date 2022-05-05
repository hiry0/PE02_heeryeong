# 2020042060 장희령
import numpy as np
a1 = np.full((3, 3), 2) # row = 3, column = 3, elements = 2
print(f'a1 = {a1}')

a2 = np.arange(1, 13)   # list range, 1 to 12
print(f'a2 = {a2}')

a3 = np.arange(3, 50, 3) # 3 to 49, 3 step
print(f'a3 = {a3}')

a4 = np.linspace(0, 20, 5) # 0 to 20, divide 5
print(f'a4 = {a4}')