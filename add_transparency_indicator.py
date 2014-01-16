import os, json, csv
from collections import defaultdict
import urllib.parse

line_mapping = {
    #11: '1.1',
    #13:
    #15: '1.3',
    21: '2.1',
    23: '2.2',
    25: '2.3',
    27: '2.4',
    29: '2.5',
    31: '3.1.1',
    33: '3.2',
    35: '5.1',
    37: '5.2',
    39: '5.3',
    41: '6.1',
    43: '6.2',
    45: '6.3.1'
}

publisher_reverse = {}
j = json.load(open('publishers.json'))
for publisher in j['result']:
    publisher_reverse[publisher['display_name']] = publisher['name']

for fname in os.listdir('in'):
    reader = csv.reader(open(os.path.join('in',fname)))
    try:
        header = reader.__next__()
    except StopIteration: continue
    name = header[0]
    if name in publisher_reverse:
        slug = publisher_reverse[name]
        publisher_tests = json.load(open('results/{0}.json'.format(slug)))['tests']
        writer = csv.writer(open(os.path.join('out',name+'.csv'), 'w'))
        for i, row in enumerate(reader):
            try:
                if i in line_mapping:
                    row[1] = publisher_tests[line_mapping[i]]['percentage']
            except KeyError as e:
                print('{0} missing for {1}'.format(e, name))
            writer.writerow(row)
    else:
        print('{0} does not match'.format(name))
