import csv
import json


jsonfile = open('napa.json', 'w')
reader = csv.reader(open('napa_data.csv', 'rU'))

result = {}
for row in reader:
    key = row[0]
    result[key] = row[1]
    #print result 

json.dump(result, jsonfile)