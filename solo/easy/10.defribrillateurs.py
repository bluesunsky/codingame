import math,csv
I=input
F=lambda x:float(x.replace(',','.'))
A,B,C=F(I()),F(I()),[I()for i in[0]*int(I())]
print(sorted([(((A-F(r[-2]))*math.cos((F(r[-1])+B)/2))**2+(B-F(r[-1]))**2,r[1])for r in csv.reader(C,delimiter=';')])[0][1])