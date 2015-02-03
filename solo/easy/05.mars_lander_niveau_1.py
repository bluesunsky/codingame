LAND=[ list(map(int,input().split())) for i in range(int(input()))]
X,Y=zip(*LAND)
x,y,hs,vs,f,r,p=map(int,input().split())
for i,xx in enumerate(X):
    if xx>x: break
SOL=Y[i]
while 1:
    R,P=0,0
    dist=y-SOL
    if vs!=0 and abs(dist/vs)<48:P=4
    print('%d %d'%(R,P))
    x, y, hs, vs, f, r, p =map(int,input().split())