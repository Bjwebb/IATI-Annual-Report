import os, csv
from collections import defaultdict
import urllib.parse

publishers = defaultdict(dict)

for sheetname in ['Other.csv', 'Signatory.csv']:
    reader = csv.reader(open(sheetname))
    header = reader.__next__()
    for row in reader:
        for i, cell in enumerate(row):
            publishers[header[i]][row[1]] = cell

line_mapping = {
    #11: '1.1',
    #13:
    #15: '1.3',
    21: '2.1',
    23: '2.2',
    25: '2.3',
    27: '2.4',
    29: '2.5',
    31: '3.1',
    33: '3.3',
    35: '5.1',
    37: '5.2',
    39: '5.3',
    41: '6.1',
    43: '6.2',
    45: '6.3'
}

for fname in os.listdir('in'):
    #name = urllib.parse.unquote(fname.split('-')[-1]).strip(' ')[:-4]
    #if name == 'UN Habitat': name = 'UN-Habitat'
    reader = csv.reader(open(os.path.join('in',fname)))
    try:
        header = reader.__next__()
    except StopIteration: continue
    name = header[0]
    if name in publishers:
        writer = csv.writer(open(os.path.join('out',name+'.csv'), 'w'))
        for i, row in enumerate(reader):
            try:
                if i in line_mapping:
                    row[1] = publishers[name][line_mapping[i]]
            except KeyError:
                print('Stats missing for {0}'.format(name))
            writer.writerow(row)
    else:
        print('{0} does not match'.format(name))
