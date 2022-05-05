import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [2, 4, 9, 17.5])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.axis([0, 5, 0, 20])
# X, Y축의 범위: [xmin, xmax, ymin, ymax]

plt.show()