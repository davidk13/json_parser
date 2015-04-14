import csv
import json

csvfile = open('san_francisco_data.csv', 'rU')
jsonfile = open('san_francisco.json', 'w')

fieldnames = ("Hour","Fare")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

