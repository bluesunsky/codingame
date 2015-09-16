while 1:
    X,H=int(raw_input().split()[0]),[input()for i in[0]*8]
    print 'FIRE'if X==sorted([(abs(X-i),i)for i,j in enumerate(H)if j==max(H)])[0][1]else'HOLD'