c=lambda a,b:(int(b),a)
while 1:print(sorted([c(*input().split())for i in range(int(input()))])[0][1])
