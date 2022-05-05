from xml.etree.ElementTree import parse
import matplotlib.pyplot as plt

tree = parse('HY202103_D08_(0,2)_LION1_DCM_LMZC.xml')
root = tree.getroot()

# IV curve
for Voltage in root.iter('Voltage'):
    v = Voltage.text
    vl = list(map(float, v.split(',')))
    print(vl)

for Current in root.iter('Current'):
    i = Current.text
    il = list(map(float, i.split(',')))
    il = list(map(abs, il))
    # il = list(map(abs, map(float, i.split(','))))
    print(il)

plt.figure(figsize = (10, 5))
plt.subplot(1, 2, 1)
plt.plot(vl, il, 'bo-', label='I-V curve')
plt.title('IV-analysis')
plt.xlabel('Voltage [V]')
plt.ylabel('Current [A]')
plt.legend(loc='best')
plt.yscale('log')

# L-IL graph
length = []
intensity = []

for L in root.iter('L'):
    l = L.text
    wl = list(map(float, l.split(',')))
    length.append(wl)

for IL in root.iter('IL'):
    il = IL.text
    il1 = list(map(float, il.split(',')))
    intensity.append(il1)

name = []
for data in root.iter('WavelengthSweep'):
    name.append(data.get('DCBias'))

for n in range(len(length)):
    plt.subplot(1, 2, 2)
    plt.title('IL-L analysis')
    plt.xlabel('Wavelength [nm]')
    plt.ylabel('Intensity [dB]')
    plt.rc('legend', fontsize=7)

    if n == 6:
        plt.plot(length[n], intensity[n], label=f'DCBias = RFE')

    else:
        plt.plot(length[n], intensity[n], label=f'DCBias = {name[n]}V')
    plt.legend(loc='best', ncol=3)
plt.savefig('그래프사진.png', dpi=300, bbox_inches='tight')
plt.show()