import numpy as np

n = int(input('n = '))
a = []
for i in range(n):
    b = list(map(int, input().split()))
    if len(b) != n:
        print('error')
    else:
        a.append(b)
print(a)
''' a 안에 먼저 넣지 않고 길이로 판별한 후 집어넣기, error가 떠도 다음 수 입력하면 그 자리로 들어가게 만들기'''
# c = list(map(int, input().split()))
# A = np.array(a)
# B = np.array(c)
# x = np.linalg.solve(A,B)
# print(x)