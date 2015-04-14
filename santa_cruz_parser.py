import csv
import json

csvfile = open('santa_cruz_data.csv', 'rU')
jsonfile = open('santa_cruz.json', 'w')

fieldnames = ("Hour","Fare")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

