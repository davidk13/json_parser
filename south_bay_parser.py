import csv
import json


jsonfile = open('south_bay.json', 'w')
reader = csv.reader(open('south_bay_data.csv', 'rU'))

result = {}
for row in reader:
    key = row[0]
    result[key] = row[1]
    #print result 

json.dump(result, jsonfile)