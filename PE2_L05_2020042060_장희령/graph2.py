import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

tree = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')
root = tree.getroot()

def spfl(a):    # spfl 함수 정의
    sp = a.text.split(',')  # ,를 기준으로 나누고 값 가져오기
    fl = list(map(float, sp))   # 가져온 값을 실수로 바꾸고 리스트에 넣기
    return fl   # fl 반환

# I-V Graph
for data in root.iter('Voltage'):
    v = spfl(data)  # 'Voltage'안에 있는 값을 spfl함수를 사용해 v에 저장
    # print(f'{data.tag}: {data.text}')
    # a = data.text.split(',')
    # b = list(map(float,a))

for data in root.iter('Current'):
    i = list(map(abs, spfl(data)))  #'Current'안에 있는 값을 spfl함수를 사용하고, 절댓값을 사용해 리스트 안에 넣어
    # print(f'{data.tag}: {data.text}')
    # c = data.text.split(',')
    # d = list(map(float,c))
    # d = list(map(abs,d))

plt.figure(figsize = (10,5))
# plt.subplots(constrained_layout = True)
plt.subplot(2,2,4)
plt.title("IV analysis")
plt.plot(v, i, 'bo--', label = 'I-V curve')
plt.xlabel("Voltage [V]")
plt.ylabel("Current [A]")
plt.legend(loc = 'best')
plt.yscale('log')

# plt.ylim([1e-11, 8e-10])

# Raw Spectrum
wvl = []
itst = []
for data in root.iter('L'):
    L1 = data.text.split(',')
    L2 = list(map(float, L1))
    wvl.append(L2)
for data in root.iter('IL'):
    IL1 = data.text.split(',')
    IL2 = list(map(float, IL1))
    itst.append(IL2)

lgds = []
for data in root.iter("WavelengthSweep"):
    lgds.append(data.get("DCBias"))

plt.subplot(2, 2, 1)
for n in range(len(wvl)):
    plt.title("Transmission spectra-as measured")
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Measured transmission [dB]")
    plt.rc("legend", fontsize = 7)
    if n == 6:
        plt.plot(wvl[6], itst[6], label = 'DCBias = REF')
    else:
        plt.plot(wvl[n], itst[n], label = f'DCBias = {lgds[n]}V')
    plt.legend(loc = 'best', ncol = 3)

# Fitting
plt.subplot(2, 2, 2)
for n in range(len(wvl)):
    if n == 6:
        plt.plot(wvl[n], itst[n], label="REF")
    else:
        continue
# for i in range(4, 7):
dp1 = np.polyfit(wvl[6], itst[6], 4)
f1 = np.poly1d(dp1)
plt.plot(wvl[6], f1(wvl[6]), 'r--', label = 'fit')
plt.legend(loc='lower right')
plt.xlabel('Wavelength[nm]')
plt.ylabel('Transmissions[dB]')
plt.title('Transmission spectra - fitted')
# def polyfit(x, y, degree):
#     results = {}
#     coeffs = np.polyfit(x, y, degree)
#     results['polynomial'] = coeffs.tolist()
#     p = np.poly1d(coeffs)
#     yhat = p(x)
#     ybar = np.sum(y)/len(y)
#     ssreg = np.sum((yhat-ybar)**2)
#     sstot = np.sum((y - ybar)**2)
#     results['determination'] = ssreg / sstot
#     return results

plt.savefig("PE2_TW02_Pic.png",dpi = 300, bbox_inches = 'tight')
plt.show()
