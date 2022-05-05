import pandas as pd
import matplotlib.pyplot as plt
from src import process

#wafer-to-wafer
time = process.nowDatetime
data = pd.read_csv('./result/csv_{}/analyzed.csv'.format(time))
y = []
wafernumber = data['Wafer']

max_spec = data['Max transmission Ref.spec.(dB)']
pos_volt = data['I at -1V']
neg_volt = data['I at 1V']

plt.figure(figsize=(16, 10))
plt.suptitle('Result of wafer-to-wafer using csv file', fontsize=20)

for i in range (len(wafernumber)):
    if str(wafernumber[i]) == 'D07':
        plt.subplot(1, 3, 1)
        plt.scatter(wafernumber[i], max_spec[i], c = 'red')
    elif str(wafernumber[i]) == 'D08':
        plt.subplot(1, 3, 1)
        plt.scatter(wafernumber[i], max_spec[i], c = 'blue')
    elif str(wafernumber[i]) == 'D23':
        plt.subplot(1, 3, 1)
        plt.scatter(wafernumber[i], max_spec[i], c = 'green')
    elif str(wafernumber[i]) == 'D24':
        plt.subplot(1, 3, 1)
        plt.scatter(wafernumber[i], max_spec[i], c = 'black')
plt.ylabel('Max transmission Fef.spec.(dB)')

for i in range(len(wafernumber)):

    if str(wafernumber[i]) == 'D07':
        plt.subplot(1, 3, 2)
        plt.scatter(wafernumber[i], pos_volt[i], c = 'red')
    elif str(wafernumber[i]) == 'D08':
        plt.subplot(1, 3, 2)
        plt.scatter(wafernumber[i], pos_volt[i], c = 'blue')
    elif str(wafernumber[i]) == 'D23':
        plt.subplot(1, 3, 2)
        plt.scatter(wafernumber[i], pos_volt[i], c = 'green')
    elif str(wafernumber[i]) == 'D24':
        plt.subplot(1, 3, 2)
        plt.scatter(wafernumber[i], pos_volt[i], c = 'black')
plt.ylabel('I at 1V')

for i in range(len(wafernumber)):

    if str(wafernumber[i]) == 'D07':
        plt.subplot(1, 3, 3)
        plt.scatter(wafernumber[i], neg_volt[i], c = 'red')
    elif str(wafernumber[i]) == 'D08':
        plt.subplot(1, 3, 3)
        plt.scatter(wafernumber[i], neg_volt[i], c = 'blue')
    elif str(wafernumber[i]) == 'D23':
        plt.subplot(1, 3, 3)
        plt.scatter(wafernumber[i], neg_volt[i], c = 'green')
    elif str(wafernumber[i]) == 'D24':
        plt.subplot(1, 3, 3)
        plt.scatter(wafernumber[i], neg_volt[i], c = 'black')
plt.ylabel('I at -1V')
plt.savefig('./result/wafer_comparison/wafer to wafer.png')
plt.show()
plt.close()