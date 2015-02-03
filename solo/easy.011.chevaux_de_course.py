P=sorted([int(input())for i in range(int(input()))])
print(min([abs(a-b)for a,b in zip(P,P[1:])]))