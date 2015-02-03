N,Q,convert=int(input()),int(input()),lambda ext,mt:(ext.upper(),mt)
exts=dict([convert(*input().split()) for i in range(N)])
for i in range(Q):
    try: print(exts.get((input().rsplit('.',1))[1].upper(),'UNKNOWN'))
    except IndexError: print('UNKNOWN')