import xml.etree.ElementTree as ET

tree = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')   # xml 파일 불러오기
root = tree.getroot()

data = ET.parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml').getroot()

# for v in root.iter('Voltage'):
#     print(f'{v.tag} : {v.text}')
# for i in root.iter('Current'):
#     print(f'{i.tag} : {i.text}')
for l in root.iter('L'):
    print(f'{l.tag} : {l.text}')
# for il in root.iter('IL'):
#     print(f'{il.tag} : {il.text}')