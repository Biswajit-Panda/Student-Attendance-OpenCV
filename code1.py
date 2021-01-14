# import csv
# import json

# csvfile = open('./attendance.csv', 'r')
# fieldnames = csvfile.readline()
# csvfile.close()
# csvfile = open('./attendance.csv', 'r')
# jsonfile = open('atten.json', 'w')
# fieldnames = fieldnames.split(',')
# print(fieldnames)
# reader = csv.DictReader( csvfile, fieldnames)
# out = json.dumps( [ row for row in reader ] )
# jsonfile.write(out)
import json

f = open('atten.json','r')
data = json.load(f)

for i in data:
    print(i)