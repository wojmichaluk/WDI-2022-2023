def addition(*args):
    (l1,m1)=args[0]
    (l2,m2)=args[1]
    m=nww(m1,m2)
    l=l1*(m//m1)+l2*(m//m2)
    return (l,m)

def sub(*args):
    (l1,m1)=args[0]
    (l2,m2)=args[1]
    return addition((l1,m1),(l2*(-1),m2))

def multi(*args):
    (l1,m1)=args[0]
    (l2,m2)=args[1]
    l=l1*l2
    m=m1*m2
    l,m=shorten((l,m))
    return (l,m)

def division(*args):
    (l1,m1)=args[0]
    (l2,m2)=args[1]
    return multi((l1,m1),(m2,l2))

def shorten(*args):
    (l,m)=args[0]
    return l//nwd(l,m),m//nwd(l,m)

def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def nww(a,b):
    return (a*b)//nwd(a,b)

def Las_Lgs(T):
    las=lgs=0
    curr_a=curr_g=1
    r=shorten(sub((T[1][0],T[1][1]),(T[0][0],T[0][1])))
    q=division((T[1][0],T[1][1]),(T[0][0],T[0][1]))
    l=T[0][0]
    m=T[0][1]
    tab=T[1:]
    for wym in tab:
        lc=wym[0]
        mc=wym[1]
        if shorten(sub((lc,mc),(l,m)))==r:
            curr_a+=1
        else:
            r=shorten(sub((lc,mc),(l,m)))
            if curr_a>=3:
                las+=1
            curr_a=2
        if division((lc,mc),(l,m))==q:
            curr_g+=1
        else:
            q=division((lc,mc),(l,m))
            if curr_g>=3:
                lgs+=1
            curr_g=2
        (l,m)=(lc,mc)
    if curr_a>=3:
        las+=1
    if curr_g>=3:
        lgs+=1
    if las>lgs:
        return 1
    elif lgs>las:
        return -1
    else:
        return 0

#T=[(1,2),(1,2),(4,8)]
#print(Las_Lgs(T))
