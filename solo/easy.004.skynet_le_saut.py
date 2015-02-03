R,G,L=map(int,(input(),input(),input()))
while 1:
    S,X=map(int,(input(),input()))
    if X>=R:       print("SLOW")
    elif X+S-1>=R: print("JUMP")
    elif S<=G:     print("SPEED")
    elif S>G+1:    print("SLOW")
    else:          print("WAIT")