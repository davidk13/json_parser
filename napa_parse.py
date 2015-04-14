import csv
import json

csvfile = open('napa.csv', 'rU')
jsonfile = open('napa.json', 'w')

fieldnames = ("Hour","Fare")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

