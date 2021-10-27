import csv
data1 = []
data2 = []
with open("dataset_1.csv","r")as f :
    reader = csv.reader(f)
    for row in reader:
        data1.append(row)
headers1 = data1 [0]
planetdata1 = data1 [1:]
with open("data2storted.csv","r")as f :
    reader = csv.reader(f)
    for row in reader:
        data2.append(row)
headers2 = data2 [0]
planetdata2 = data2 [1:]
headers = headers1+headers2
planetdata = []
for i,d in enumerate(planetdata1):
    planetdata.append(planetdata1[i]+planetdata2[i])
with open("final.csv","a+")as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planetdata)