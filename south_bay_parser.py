import csv
import json

csvfile = open('south_bay_data.csv', 'rU')
jsonfile = open('south_bay.json', 'w')

fieldnames = ("Hour","Fare")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

