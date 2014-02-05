import os, json, csv
from collections import defaultdict
import urllib.parse

line_mapping = {
    11: '1.1',
    #13:
    15: '1.3',
    17: '1.4.1',
    19: '1.4.2',
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

extra_tests = defaultdict(dict)

reader = csv.reader(open('csv/Timeliness_Transactions_1.1.csv'))
for row in reader:
    if len(row) > 20:
        extra_tests[row[0]]['1.1'] = row[20]
reader = csv.reader(open('csv/Activity_planning_3.csv'))
for row in reader:
    if len(row) > 4:
        extra_tests[row[0]]['1.3'] = row[4]
reader = csv.reader(open('csv/Alignement_with_financial_year_Transactions_4.1.csv'))
for row in reader:
    if len(row) > 24:
        extra_tests[row[0]]['1.4.1'] = row[24]
reader = csv.reader(open('csv/Alignement_with_financial_year_Budgets_4.2.csv'))
for row in reader:
    if len(row) > 11:
        extra_tests[row[0]]['1.4.2'] = row[11]

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
            if i in line_mapping:
                test = line_mapping[i]
                if test in publisher_tests:
                    row[1] = publisher_tests[test]['percentage']
                elif test in extra_tests[slug]:
                    row[1] = extra_tests[slug][test]
                else:
                    print('{0} missing for {1}'.format(test, name))
            writer.writerow(row)
    else:
        print('{0} does not match'.format(name))
