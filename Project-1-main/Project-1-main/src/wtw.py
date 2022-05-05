import pandas as pd
import matplotlib.pyplot as plt
from . import path
from . import directory
import warnings


# wafer-to-wafer
def analyze(time):
    warnings.filterwarnings(action='ignore')
    data = pd.read_csv('./result/csv_{}/analyzed.csv'.format(time))
    y = []
    wafernumber = data['Wafer']

    max_spec = data['Max transmission of Ref. spec. (dB)']
    pos_volt = data['I at -1V [A]']
    neg_volt = data['I at 1V[A]']
    wavelength = data['Analysis Wavelength']

    plt.figure(figsize=(16, 10))
    plt.suptitle('Result of wafer-to-wafer using csv file', fontsize=20)

    for i in range(len(wafernumber)):
        if str(wavelength[i]) == '1550':
            plt.subplot(2, 3, 1)
            if str(wafernumber[i]) == 'D07':
                plt.scatter(wafernumber[i], max_spec[i], c='red')
            elif str(wafernumber[i]) == 'D08':
                plt.scatter(wafernumber[i], max_spec[i], c='blue')
            elif str(wafernumber[i]) == 'D23':
                plt.scatter(wafernumber[i], max_spec[i], c='green')
            elif str(wafernumber[i]) == 'D24':
                plt.scatter(wafernumber[i], max_spec[i], c='black')
            plt.title('Max transmission Fef.spec. in 1550nm')
            plt.ylabel('dB')
        else:
            plt.subplot(2, 3, 4)
            if str(wafernumber[i]) == 'D07':
                plt.scatter(wafernumber[i], max_spec[i], c='red')
            elif str(wafernumber[i]) == 'D08':
                plt.scatter(wafernumber[i], max_spec[i], c='blue')
            elif str(wafernumber[i]) == 'D23':
                plt.scatter(wafernumber[i], max_spec[i], c='green')
            elif str(wafernumber[i]) == 'D24':
                plt.scatter(wafernumber[i], max_spec[i], c='black')
            plt.title('Max transmission Fef.spec. in 1310nm')
            plt.ylabel('dB')

    for i in range(len(wafernumber)):
        if str(wavelength[i]) == '1550':
            plt.subplot(2, 3, 2)
            if str(wafernumber[i]) == 'D07':
                plt.scatter(wafernumber[i], pos_volt[i], c='red')
            elif str(wafernumber[i]) == 'D08':
                plt.scatter(wafernumber[i], pos_volt[i], c='blue')
            elif str(wafernumber[i]) == 'D23':
                plt.scatter(wafernumber[i], pos_volt[i], c='green')
            elif str(wafernumber[i]) == 'D24':
                plt.scatter(wafernumber[i], pos_volt[i], c='black')
            plt.title('I at 1V in 1550nm')
            plt.ylabel('Current[A]')
        else:
            plt.subplot(2, 3, 5)
            if str(wafernumber[i]) == 'D07':
                plt.scatter(wafernumber[i], pos_volt[i], c='red')
            elif str(wafernumber[i]) == 'D08':
                plt.scatter(wafernumber[i], pos_volt[i], c='blue')
            elif str(wafernumber[i]) == 'D23':
                plt.scatter(wafernumber[i], pos_volt[i], c='green')
            elif str(wafernumber[i]) == 'D24':
                plt.scatter(wafernumber[i], pos_volt[i], c='black')
            plt.title('I at 1V in 1310nm')
            plt.ylabel('Current[A]')

    for i in range(len(wafernumber)):
        if str(wavelength[i]) == '1550':
            plt.subplot(2, 3, 3)
            if str(wafernumber[i]) == 'D07':
                plt.scatter(wafernumber[i], neg_volt[i], c='red')
            elif str(wafernumber[i]) == 'D08':
                plt.scatter(wafernumber[i], neg_volt[i], c='blue')
            elif str(wafernumber[i]) == 'D23':
                plt.scatter(wafernumber[i], neg_volt[i], c='green')
            elif str(wafernumber[i]) == 'D24':
                plt.scatter(wafernumber[i], neg_volt[i], c='black')
            plt.title('I at -1V in 1550nm')
            plt.ylabel('Current[A]')
        else:
            plt.subplot(2, 3, 6)
            if str(wafernumber[i]) == 'D07':
                plt.scatter(wafernumber[i], neg_volt[i], c='red')
            elif str(wafernumber[i]) == 'D08':
                plt.scatter(wafernumber[i], neg_volt[i], c='blue')
            elif str(wafernumber[i]) == 'D23':
                plt.scatter(wafernumber[i], neg_volt[i], c='green')
            elif str(wafernumber[i]) == 'D24':
                plt.scatter(wafernumber[i], neg_volt[i], c='black')
            plt.title('I at -1V in 1310nm')
            plt.ylabel('Current[A]')

    save_path = path.path() + '/result'
    directory.create_folder(save_path)

    plt.savefig(save_path + '/wafer_to_wafer.png')
    plt.show()
