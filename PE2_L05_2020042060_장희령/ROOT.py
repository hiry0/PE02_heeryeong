import xml.etree.ElementTree as ET

tree = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')   # xml 파일 불러오기
root = tree.getroot()
#
# Voltage
# v = root[6][0][0][2][1][0].text
# print(f'Voltage : {v}')
# #Current
# i = root[6][0][0][2][1][1].text
# print(f'Current : {i}')
# L
for i in range(2, 8):
    for a in range(0,2):
        n = root[6][0][0][2][i][a]
        print(f'{n.tag}{i-1} : {n.text}')
# for i in range(2, 8):
#     wl = root[6][0][0][2][i][0]
#     print(f'{wl.tag}{i-1} : {wl.text}')

# wl1 = root[6][0][0][2][2][0].text
# wl2 = root[6][0][0][2][3][0].text
# wl3 = root[6][0][0][2][4][0].text
# wl4 = root[6][0][0][2][5][0].text
# wl5 = root[6][0][0][2][6][0].text
# wl6 = root[6][0][0][2][7][0].text
# print(f'L1 = {wl1}\nL2 = {wl2}\nL3 = {wl3}\nL4 = {wl4}\nL5 = {wl5}\nL6 = {wl6}\n')

# # IL
# for i in range(2, 8):
#     il = root[6][0][0][2][i][1]
#     print(f'{il.tag}{i-1} : {il.text}')
# il1 = root[6][0][0][2][2][1].text
# il2 = root[6][0][0][2][3][1].text
# il3 = root[6][0][0][2][4][1].text
# il4 = root[6][0][0][2][5][1].text
# il5 = root[6][0][0][2][6][1].text
# il6 = root[6][0][0][2][7][1].text
# print(f'IL1 = {il1}\nIL2 = {il2}\nIL3 = {il3}\nIL4 = {il4}\nIL5 = {il5}\nIL6 = {il6}\n')