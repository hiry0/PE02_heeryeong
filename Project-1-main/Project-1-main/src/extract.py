import pandas
import xml.etree.ElementTree as ET
from dateutil.parser import parse
import os
from . import graph
from . import path
from . import directory


def data_save(route, time):
    tree = ET.parse(route)
    root = tree.getroot()

    columns = ['Lot', 'Wafer', 'Mask', 'TestSite', 'Name', 'Date', 'Row', 'Column', 'ErrorFlag', 'Error description', 'Analysis Wavelength', 'Rsq of Ref. spectrum (Nth)', 'Max transmission of Ref. spec. (dB)', 'Rsq of IV', 'I at -1V [A]', 'I at 1V[A]']
    #  'Script ID', 'Script Version', 'Script Owner',
    #  스크립트 정보

    data = []
    values = []

    TestSiteInfo = root.find('TestSiteInfo').attrib
    values.append(TestSiteInfo['Batch'])
    values.append(TestSiteInfo['Wafer'])
    values.append(TestSiteInfo['Maskset'])
    values.append(TestSiteInfo['TestSite'])
    Modulator = root.find('.//Modulator')
    values.append(Modulator.attrib['Name'])
    PortCombo = Modulator.find('PortCombo')
    values.append(parse(PortCombo.attrib['DateStamp']))
    values.append(TestSiteInfo['DieRow'])
    values.append(TestSiteInfo['DieColumn'])

    voltage = list(map(float, root.find('.//IVMeasurement/Voltage').text.split(',')))
    current = list(map(float, root.find('.//IVMeasurement/Current').text.split(',')))


    if graph.ref_max_Rsq >= 0.995 and current[12] < (-(10 ** -4)):
        ErrorFlag = 0
        ErrorDescription = 'No Error'
    elif graph.ref_max_Rsq < 0.995 and current[12] < (-(10 ** -4)):
        ErrorFlag = 1
        ErrorDescription = 'Ref. spec. Error'
    elif graph.ref_max_Rsq >= 0.995 and current[12] >= (-(10 ** -4)):
        ErrorFlag = 2
        ErrorDescription = 'IV-fitting'
    else:
        ErrorFlag = 3
        ErrorDescription = 'Ref. spec. Error. IV-fitting'


    values.append(ErrorFlag)
    values.append(ErrorDescription)
    values.append(root.find(".//DesignParameter[@Name='Design wavelength']").text)
    values.append(graph.ref_max_Rsq)
    values.append(graph.max_IL)

    voltage = list(map(float, root.find('.//IVMeasurement/Voltage').text.split(',')))
    current = list(map(float, root.find('.//IVMeasurement/Current').text.split(',')))
    index1 = voltage.index(-1)
    index2 = voltage.index(1)
    values.append(graph.IV_max_rsq)
    values.append(current[index1])
    values.append(current[index2])

    # 스크립트 정보 추가 필요

    data.append(values)
    df = pandas.DataFrame(data, columns=columns).set_index("Lot")
    save_route = path.path() + '/result/csv_{}'.format(time)
    directory.create_folder(save_route)
    if not os.path.exists(save_route + '/analyzed.csv'):
        df.to_csv(save_route + '/analyzed.csv', mode='w')
    else:
        df.to_csv(save_route + '/analyzed.csv', mode='a', header=False)
