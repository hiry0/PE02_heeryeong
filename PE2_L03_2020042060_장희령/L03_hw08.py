# 2020042060 장희령
import numpy as np
n = int(input('n = '))  # n is input as an integer
a = []  # blank list a
for i in range(n):  # i is a number from 0 to (n-1)
    a.append(list(map(int, input().split())))   # divide the integers entered in list a into spaces and put them in the list a
    if len(a[i]) != n:  # if the length of element a with index i is not n
        print('error')  # print error
b = list(map(int, input().split())) # divide the integers entered in list a into spaces
A = np.array(a)
B = np.array(b)
x = np.linalg.solve(A,B)    # solution of an equation
print(x)

'''
11 7 8 -4 -2
9 -8 5 11 -4
1 13 -10 2 1
-3 1 1 -1 2
21 -7 -5 1 7
23 32 10 8 31
'''