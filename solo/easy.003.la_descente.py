while 1:
 X,H=int(input().split()[0]),[int(input())for i in range(8)]
 h=max(H)
 print('FIRE'if X==sorted([(abs(X-i),i)for i,j in enumerate(H)if j==h])[0][1]else'HOLD')