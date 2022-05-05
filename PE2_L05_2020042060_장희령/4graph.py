import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
from lmfit import Model
from sklearn.metrics import r2_score

tree = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')
root = tree.getroot()

def spfl(a):    # spfl 함수 정의
    sp = a.text.split(',')  # ,를 기준으로 나누고 값 가져오기
    fl = list(map(float, sp))   # 가져온 값을 실수로 바꾸고 리스트에 넣기
    return fl   # fl 반환

def IV(x, Is):
    return Is * (exp(x / 0.026) - 1)

# r**2
def polyfit(x, y, degree):
    results = {}
    coeffs = np.polyfit(x, y, degree)
    results['polynomial'] = coeffs.tolist()
    p = np.poly1d(coeffs)
    yhat = p(x)
    ybar = np.sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)
    sstot = np.sum((y - ybar)**2)
    results['determination'] = ssreg / sstot
    return results
# 3차
# I-V Graph
for data in root.iter('Voltage'):
    vlt = spfl(data)  # 'Voltage'안에 있는 값을 spfl함수를 사용해 v에 저장
    v = np.array(vlt)
    # print(f'{data.tag}: {data.text}')
    # a = data.text.split(',')
    # b = list(map(float,a))
for data in root.iter('Current'):
    crt = list(map(abs, spfl(data)))  #'Current'안에 있는 값을 spfl함수를 사용하고, 절댓값을 사용해 리스트 안에 넣어
    c = np.array(crt)
    # print(f'{data.tag}: {data.text}')
    # c = data.text.split(',')
    # d = list(map(float,c))
    # d = list(map(abs,d))
plt.figure(figsize = (12, 8))

plt.subplot(2,2,4)
v = np.array(vlt)
i = np.array(crt)
gmodel = Model(IV)
# 예상 이름을 가진 매개변수 생성(매개변수, 초기 값 등)(독립변수, 함수 위치 인수)
params = gmodel.make_params(Is = 1)   # 초기 값 설정
# print(f'parameter names : {gmodel.param_names}')
# print(f'independent variables : {gmodel.independent_vars}')
result = gmodel.fit(i, params, x = v)   # 함수 모델을 데이터에 맞춘 것



c = i - result.best_fit
IV_Rsq = {}
for a in range(1, 10):
    poly = polyfit(v, c, a)
    IV_Rsq[a] = poly['determination']
IV_max_key = max(IV_Rsq, key=lambda key: IV_Rsq[key])
global IV_max_rsq
IV_max_rsq = IV_Rsq[IV_max_key]
polyIV = np.poly1d(np.polyfit(v, c, IV_max_key))(v)

plt.plot(vlt, crt, 'o', label = 'I-V curve')
plt.plot(vlt, abs(result.best_fit + polyIV), '-', label = 'I-V Fitting')
# 'darkorange'
# 컬러 설정 안하면 pdf 그대로 색이 나옴
plt.title("IV analysis")
plt.xlabel("Voltage [V]")
plt.ylabel("Current [A]")
plt.yscale('log')
plt.legend(loc = 'best')

# Raw data
wvl = []
itst = []
for data in root.iter('L'):
    L = spfl(data)
    # L1 = data.text.split(',')
    # L2 = list(map(float, L1))
    wvl.append(L)
for data in root.iter('IL'):
    IL = spfl(data)
    # IL1 = data.text.split(',')
    # IL2 = list(map(float, IL1))
    itst.append(IL)

lgds = []
for data in root.iter("WavelengthSweep"):
    lgds.append(data.get("DCBias"))

plt.subplot(2, 2, 1)
for n in range(len(wvl)):
    plt.title("Transmission spectra-as measured")
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Measured transmission [dB]")
    plt.rc("legend", fontsize=7)
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
dp1 = np.polyfit(wvl[6], itst[6], 3)
f1 = np.poly1d(dp1)
plt.plot(wvl[6], f1(wvl[6]), 'r--', label = 'Fit ref polynomial')

first = np.polyfit(vlt,crt,12)
second = np.polyval(first, vlt)

print(r2_score((itst[6]),f1(wvl[6])))
# 피팅 제곱의 값 즉, 1에 가까울 수록 정확하다.

plt.xlabel('Wavelength[nm]')
plt.ylabel('Transmissions[dB]')
plt.title('Transmission spectra - fitted')
plt.legend(loc='best')
plt.rc("legend", fontsize=7)

plt.subplot(2, 2, 3)
for k in range(len(wvl)-1):
    plt.title("Fitting Function")
    plt.xlabel("Wavelength [nm]")
    plt.ylabel("Measured transmission [dB]")
    plt.plot(wvl[k], itst[k] - f1(wvl[k]), label = f'DCBias = {lgds[k]}V')
    plt.legend(loc = 'best', ncol = 3)

# plt.subplots_adjust(left = 0.125, bottom = 0.2, right = 0.9, top = 0.9, wspace = 0.45, hspace = 0.5)
plt.tight_layout()
plt.savefig("4graph.png",dpi = 300, bbox_inches = 'tight')
plt.show()
