N,Q=int(input()),int(input())
E={}
for i in[0]*N:a=input().split();E[a[0].upper()]=a[1]
for i in[0]*Q:
    try:print(E[(input().rsplit('.',1))[1].upper()])
    except:print('UNKNOWN')