import csv
import json

csvfile = open('east_bay_data.csv', 'rU')
jsonfile = open('east_bay.json', 'w')

fieldnames = ("Hour","Fare")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

