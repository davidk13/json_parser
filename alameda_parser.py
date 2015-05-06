import csv
import json


jsonfile = open('alameda.json', 'w')
reader = csv.reader(open('alameda_csv.csv', 'rU'))

result = {}
for row in reader:
    key = row[0]
    result[key] = row[1]
    #print result 

json.dump(result, jsonfile)