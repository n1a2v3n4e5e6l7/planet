import csv
from os import read
data = []
with open("dataset_2.csv","r")as f :
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
headers = data [0]
planetdata = data [1:]
for d in planetdata:
    d[2] = d[2].lower()
planetdata.sort(key=lambda planetdata: planetdata[2])
with open("data2_storted.csv","w")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)