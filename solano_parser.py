import csv
import json


jsonfile = open('solano.json', 'w')
reader = csv.reader(open('solano_csv.csv', 'rU'))

result = {}
for row in reader:
    key = row[0]
    result[key] = row[1]
    #print result 

json.dump(result, jsonfile)