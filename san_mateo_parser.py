import csv
import json


jsonfile = open('san_mateo.json', 'w')
reader = csv.reader(open('san_mateo_csv.csv', 'rU'))

result = {}
for row in reader:
    key = row[0]
    result[key] = row[1]
    #print result 

json.dump(result, jsonfile)