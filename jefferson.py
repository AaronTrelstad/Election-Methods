import csv
import math

with open('data.csv') as f:
    reader = csv.reader(f)
    datapoints = list(reader)

s = 0
for i in range(len(datapoints)):
    s+=int(datapoints[i][1])

idealratio = s / 435

for i in range(len(datapoints)):
    datapoints[i].append(math.floor(int(datapoints[i][1])/idealratio))

for i in range(len(datapoints)):
    datapoints[i].append(int(datapoints[i][1])/(datapoints[i][2]+1))

datapoints = sorted(datapoints, key=lambda x:x[3], reverse=True)

intial = 0
for i in range(len(datapoints)):
    intial += datapoints[i][2]

for i in range(0, 435-intial+1):
    datapoints[i][2] += 1

datapoints = sorted(datapoints, key=lambda x:x[2], reverse=True)

ans = []
for i in range(len(datapoints)):
    ans.append([datapoints[i][0], datapoints[i][2] + 2])

print(ans)