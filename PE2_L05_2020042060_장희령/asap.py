import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import ExponentialModel
from sklearn.metrics import r2_score

tree = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')
root = tree.getroot()

def snf(a):
    splt = a.text.split(',')
    flst = list(map(float,splt))
    return flst


for data in root.iter('Voltage'):
    x = np.array(snf(data))

for data in root.iter('Current'):
    crt = list(map(abs,snf(data)))
    y = np.array(crt)

regressor = ExponentialModel()
initial_guess = dict(amplitude=1, decay=-1)
results = regressor.fit(y, x=x, **initial_guess)
y_fit = results.best_fit

plt.plot(x, y, "o", label="Data")
plt.plot(x, y_fit, "r--", label="Fit")
plt.legend()
plt.yscale("log")
print(r2_score(x, y_fit))

plt.show()
