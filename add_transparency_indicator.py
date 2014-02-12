import os, json, csv
from collections import defaultdict, OrderedDict
from functools import partial
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

summary_tests = ['1.1', '1.3', '1.4.1', '1.4.2', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '3.1.1', '3.1.2', '3.2', '5.1', '5.2', '5.3', '6.1', '6.2', '6.3.1', '6.3.2' ]

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
        extra_tests[row[0]]['1.4.1'] = row[24].replace('Quaterly', 'Quarterly')
reader = csv.reader(open('csv/Alignement_with_financial_year_Budgets_4.2.csv'))
for row in reader:
    if len(row) > 11:
        extra_tests[row[0]]['1.4.2'] = row[11].title()

publisher_reverse['UK: FCO, Home Office, Work & Pensions, Energy & Climate Change, Health'] = 'uk'
publisher_reverse['EU Enlargement and FPI'] = 'eu-ec'

publishing_members = []

def get_test(publisher_tests, test):
    if test in publisher_tests:
        return publisher_tests[test]['percentage']
    elif test in extra_tests[slug]:
        return extra_tests[slug][test]
    else:
        print('{0} missing for {1}'.format(test, name))

summary = csv.writer(open('summary.csv', 'w'))
header_tests = json.load(open('results/aai.json'))['tests']
summary.writerow(['','Total number of activities']+[header_tests[x]['title']  if x in header_tests else '' for x in summary_tests])
summary.writerow(['','']+summary_tests)

for fname in os.listdir('in'):
    reader = csv.reader(open(os.path.join('in',fname)))
    try:
        header = reader.__next__()
    except StopIteration: continue
    name = header[0]
    if name in publisher_reverse:
        slug = publisher_reverse[name]
        publishing_members.append((slug,name))
        publisher_json = json.load(open('results/{0}.json'.format(slug)))
        publisher_tests = publisher_json['tests']
        writer = csv.writer(open(os.path.join('out',name+'.csv'), 'w'))
        for i, row in enumerate(reader):
            if i in line_mapping:
                test = line_mapping[i]
                row[1] = get_test(publisher_tests, test)
            writer.writerow(row)

        summary.writerow([name,publisher_json['activityCount']]+list(map(partial(get_test, publisher_tests), summary_tests)))
    else:
        print('{0} does not match'.format(name))
        writer = csv.writer(open(os.path.join('out',name+'.csv'), 'w'))
        for i, row in enumerate(reader):
            writer.writerow(row)

