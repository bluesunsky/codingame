LX,LY,TX,TY=[int(i) for i in input().split()]
while input():
    dx,dy=LX-TX,LY-TY
    d=max(abs(dx),abs(dy))
    dx/=d
    dy/=d
    cmd=''
    if   dy>= 0.5: cmd+='S';TY+=1
    elif dy<=-0.5: cmd+='N';TY-=1
    if   dx>= 0.5: cmd+='E';TX+=1
    elif dx<=-0.5: cmd+='W';TX-=1
    print(cmd)