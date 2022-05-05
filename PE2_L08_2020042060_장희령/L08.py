import graph as g
import pandas as pd

tree = g.ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')
root = tree.getroot()

columns = ['Lot', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date', 'Script Owner', 'Operator', 'Row', 'Column', 'ErrorFlag', 'Error description', 'Analysis Wavelength', 'Rsq of Ref. spectrum (Nth)', 'Max transmission of Ref. spec. (dB)', 'Rsq of Left IV','Rsq of right IV', 'I at -1V [A]', 'I at 1V[A]']
# 'Script ID', 'Script Version'
data = []
values = []

TestSiteInfo = root.find('TestSiteInfo').attrib
values.append(TestSiteInfo['Batch'])
values.append(TestSiteInfo['Wafer'])
values.append(TestSiteInfo['Maskset'])
values.append(TestSiteInfo['TestSite'])
DeviceInfo = root.find('.//DeviceInfo')
values.append(DeviceInfo.attrib['Name'])
PortCombo = root.find('.//PortCombo')
values.append(PortCombo.attrib['DateStamp'])
values.append('A3')
ModulatorSite = root.find('.//ModulatorSite')
values.append(ModulatorSite.attrib['Operator'])
values.append(TestSiteInfo['DieRow'])
values.append(TestSiteInfo['DieColumn'])
values.append('0')
values.append('No Error')
# wl = root[6][0][0][1][0][1]
# values.append(wl.text)
values.append(root.find(".//DesignParameter[@Name='Design wavelength']").text)
values.append(round(g.ref_rsq, 4))  # ref rsq
values.append(g.ref_max) # ref max
values.append(g.IV_left_rsq) # rsq left
values.append(g.IV_right_rsq) # rsq right
index1 = g.vlt.index(-1)    # voltage -1V 인덱스 구하기
index2 = g.vlt.index(1)     # voltage -V 인덱스 구하기
values.append(g.crt1[index1]) # I at -1V
values.append(g.crt1[index2]) # I at 1V
# print(values)

data.append(values)
df = pd.DataFrame(data, columns=columns).set_index('Lot')
print(df)

df.to_csv('df1.csv', mode = 'w')