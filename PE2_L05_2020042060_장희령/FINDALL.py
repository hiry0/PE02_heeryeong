import xml.etree.ElementTree as ET

tree = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')   # xml 파일 불러오기
root = tree.getroot()

# for v in root.findall('./ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement/Voltage'):
for v in root.findall('.//Voltage'):
    print(f'{v.tag} : {v.text}')

for i in root.findall('.//Current'):
    print(f'{i.tag} : {i.text}')

for l in root.findall('.//L'):
    print(f'{l.tag} : {l.text}')

for il in root.findall('.//IL'):
    print(f'{il.tag} : {il.text}')