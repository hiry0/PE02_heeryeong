import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [2,3,5,10], label='Price ($)')
plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.legend(loc=(0.5, 0.5))

plt.show()