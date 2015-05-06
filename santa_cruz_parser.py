import csv
import json


jsonfile = open('santa_cruz.json', 'w')
reader = csv.reader(open('santa_cruz_csv.csv', 'rU'))

result = {}
for row in reader:
    key = row[0]
    result[key] = row[1]
    #print result 

json.dump(result, jsonfile)