import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np


tree = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')
root = tree.getroot()

# def spfl(a):
#     sp = a.text.split(',')
#     fl = list(map(float, sp))
#     return fl
#
# for data in root.iter('L'):
#     L1 = data.text.split(',')
#     print(len(L1))

for data in root.iter('Current'):
    # print(f'{data.tag}: {data.text}')
    c = data.text.split(',')
    print(c)
    d = list(map(float,c))
    d = list(map(abs,d))
    print(d)

