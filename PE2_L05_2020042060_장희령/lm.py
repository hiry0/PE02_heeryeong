import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
from lmfit import Model
from sklearn.metrics import r2_score
import time

tree = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')
root = tree.getroot()

def spfl(a):    # spfl 함수 정의
    sp = a.text.split(',')  # ,를 기준으로 나누고 값 가져오기
    fl = list(map(float, sp))   # 가져온 값을 실수로 바꾸고 리스트에 넣기
    return fl   # fl 반환

def IV(x, Is, Vt):
    return Is * (exp(x / Vt) - 1)

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

for data in root.iter('Voltage'):
    vlt = spfl(data)  # 'Voltage'안에 있는 값을 spfl함수를 사용해 v에 저장
    v = np.array(vlt)

for data in root.iter('Current'):
    crt = spfl(data)  #'Current'안에 있는 값을 spfl함수를 사용하고, 절댓값을 사용해 리스트 안에 넣어
    c = np.array(crt)

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

print(r2_score(v, c))

plt.show()

# gmodel = Model(IV)
# params = gmodel.make_params(Is=1, Vt = 1)
# c = abs(i)
# result = gmodel.fit(c, params, x=v)

# plt.plot(v, result.best_fit, '--', label='Fit')
# plt.plot(v, c, 'o', label='Data')