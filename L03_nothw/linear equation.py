import numpy as np

a = np.array([[2, 3], [1, -2]])
b = np.array([1, 4])
x = np.linalg.solve(a, b)
print(x)