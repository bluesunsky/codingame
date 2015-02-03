L,H,T = int(input()),int(input()),input().upper()
ROWS=[input() for i in range(H)]
indexes='ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
RES=['']*H
for t in T:
    try:    pos=indexes.index(t)
    except: pos=len(indexes)-1
    for r in range(H): RES[r]+=ROWS[r][pos*L:(pos+1)*L]
print('\n'.join(RES))