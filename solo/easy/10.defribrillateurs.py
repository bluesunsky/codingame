import math, csv
LON,LAT,CSV,liste=float(input().replace(',','.')),float(input().replace(',','.')),[input() for i in range(int(input()))],[]
for line in csv.reader(CSV,delimiter=';'):
    lon,lat=float(line[-2].replace(',','.')),float(line[-1].replace(',','.'))
    liste.append((((LON-lon)*math.cos((lat-LAT)/2.))**2+(LAT-lat)**2,line[1]))
print(sorted(liste)[0][1])