from xml.etree.ElementTree import parse
import matplotlib.pyplot as plt

tree = parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')
root = tree.getroot()

# data
# for l in root.findall('.//L'):
#     print(f'{l.tag} : {l.text}')
# for il in root.findall('.//IL'):
#     print(f'{il.tag} : {il.text}')

def graph():
    voltage = root.find('.//Voltage')
    current = root.find('.//Cuttent')
    def flst(a):
        nonlocal voltage, current
        rst = a.text.split(',')
        dfg = list(map(float, rst))
        return dfg
        # I-V graph
    v = flst(voltage)
    # i = flst(abs(current))
    print(v)
    # print(i)
graph()


# fig = plt.figure()
#
# plt.plot(vl, il, label='I-V curve')
# plt.xlabel('Voltage [V]')
# plt.ylabel('Current [A]')
# plt.title('IV-analysis')
# plt.legend(loc='best')
# plt.yscale('log')
#
#
# plt.subplot(1, 2, 1)
# TestSiteInfo = root.find('TestSiteInfo')
# TestSite = TestSiteInfo.attrib['TestSite']
# ModulatorName = ".//*[@Name='{}_ALIGN']//".format(TestSite)
# ref_L = list(map(float, root.findtext(str(str(ModulatorName + 'L'))).split(',')))
# ref_IL = list(map(float, root.findtext(str(str(ModulatorName + 'IL'))).split(',')))
# global max_IL
# max_IL = max(ref_IL)
# for wavelengthsweep in root.iter('WavelengthSweep'):
#     L = list(map(float, wavelengthsweep.findtext('L').split(',')))
#     IL = list(map(float, wavelengthsweep.findtext('IL').split(',')))
#     if IL == ref_IL:
#         name = 'Reference'
#     else:
#         name = 'DCBias=' + str(wavelengthsweep.attrib['DCBias']) + 'V'
#     plt.plot(L, IL, 'o', label=name)
#
# plt.legend(loc='lower right')
# plt.xlabel('Wavelength[nm]')
# plt.ylabel('Measured transmissions[dB]')
# plt.title('Transmission spectra - as measured')
