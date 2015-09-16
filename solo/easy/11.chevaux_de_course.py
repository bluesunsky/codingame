p=sorted([int(input())for i in[0]*(int(input()))])
print(min([abs(a-b)for a,b in zip(p,p[1:])]))