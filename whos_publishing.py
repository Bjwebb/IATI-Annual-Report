import json, csv
from stats import elements

"""
This code was created by Ben Webb, and is released under CC0
http://creativecommons.org/publicdomain/zero/1.0/

"""

elements = sorted(elements)
out = []
out.append(['id','name']+elements)

j = json.load(open('publishers.json'))
for publisher in j['result']:
    name = publisher['display_name']
    slug = publisher['name']

    try:
        stats = json.load(open('aggregated/{0}.json'.format(slug)))
        out.append([slug,name]+[1 if stats['elements_annual_report'].get(x) else 0 for x in elements])
    except FileNotFoundError:
        pass

writer = csv.writer(open('whos_publishing.csv', 'w'))
for line in zip(*out):
    writer.writerow(line)
