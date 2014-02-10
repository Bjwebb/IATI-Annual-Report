import os, json, csv
from collections import defaultdict, OrderedDict
import urllib.parse

line_mapping = {
    11: '1.1',
    #13:
    #15: '1.3',
    15: '1.4.1',
    17: '1.4.2',
    19: '2.1',
    21: '2.2',
    23: '2.3',
    25: '2.4',
    27: '2.5',
    29: '3.1.1',
    31: '3.2',
    33: '5.1',
    35: '5.2',
    37: '5.3',
    39: '6.1',
    41: '6.2',
    43: '6.3.1'
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
        extra_tests[row[0]]['1.4.2'] = row[11].title()

publisher_reverse['UK: FCO, Home Office, Work & Pensions, Energy & Climate Change, Health'] = 'uk'
publisher_reverse['EU Enlargement and FPI'] = 'eu-ec'

publishing_members = []

for fname in os.listdir('in'):
    reader = csv.reader(open(os.path.join('in',fname)))
    try:
        header = reader.__next__()
    except StopIteration: continue
    name = header[0]
    if name in publisher_reverse:
        slug = publisher_reverse[name]
        publishing_members.append((slug,name))
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
        writer = csv.writer(open(os.path.join('out',name+'.csv'), 'w'))
        for i, row in enumerate(reader):
            writer.writerow(row)

