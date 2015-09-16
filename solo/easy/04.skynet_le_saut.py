R,G,L=map(int,(input(),input(),input()))
p=print
while 1:
    S,X=map(int,(input(),input()))
    if X>=R:p("SLOW")
    elif X+S-1>=R:p("JUMP")
    elif S<=G:p("SPEED")
    elif S>G+1:p("SLOW")
    else:p("WAIT")