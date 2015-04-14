import csv
import json

csvfile = open('marin_data.csv', 'rU')
jsonfile = open('marin.json', 'w')

fieldnames = ("Hour","Fare")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

