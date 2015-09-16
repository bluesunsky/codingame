L,H,T=int(input()),int(input()),input().upper()
R=['']*H
D=list(map(input,R))
for t in T:
    p=ord(t)
    if not 64<p<91:p=91
    for r in range(H):R[r]+=D[r][(p-65)*L:(p-64)*L]
print(*R,sep='\n')