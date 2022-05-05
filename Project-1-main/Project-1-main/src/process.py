import glob
from glob import glob
from tqdm import tqdm
from . import path
from . import graph
from . import extract
import datetime
import os
from tqdm import tqdm
from . import wtw


now = datetime.datetime.now()
nowDatetime = now.strftime('%Y%m%d_%H%M%S')


def work(wafer, coordinate, save, show, csv, data_path):
    file = []
    if data_path == '':
        if wafer == 'All' and coordinate == 'All':
            file = glob(path.path() + '/data/**/*LMZ*.xml', recursive=True)
        elif coordinate == 'All':
            file = glob(path.path() + '/data/**/{}/**/*LMZ*.xml'.format(wafer), recursive=True)
        else:
            file = glob(path.path() + '/data/**/{}/**/*{}*LMZ*.xml'.format(wafer, coordinate), recursive=True)
    else:
        if wafer == 'All' and coordinate == 'All':
            file = glob(data_path + '/**/*LMZ*.xml', recursive=True)
        elif coordinate == 'All':
            file = glob(data_path + '/**/{}/**/*LMZ*.xml'.format(wafer), recursive=True)
        else:
            file = glob(data_path + '/**/{}/**/*{}*LMZ*.xml'.format(wafer, coordinate), recursive=True)

    if not file:
        raise ValueError('Could not find data')

    for i in tqdm(file):
        graph.graph(i, save, show, nowDatetime)
        if csv is True:
            extract.data_save(i, nowDatetime)
    if csv is True:
        wtw.analyze(nowDatetime)


def open():
    os.startfile(path.path() + '/result')
