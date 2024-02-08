def ulamek(s):
    p1=s.find('.')
    p2=s.find('(')
    l1=int(s[:p1])
    m1=1
    if p1==-1:
        (l1,m1)=(int(s),1)
        (l2,m2)=(0,1)
        (l3,m3)=(0,1)
    else:
        if p2==-1:
            (l2,m2)=(int(s[p1+1:]),10**(len(s)-p1-1))
            (l3,m3)=(0,1)
        else:
            if p2-p1==1:
                (l2,m2)=(0,1)
            else:
                (l2,m2)=(int(s[p1+1:p2]),10**(p2-p1-1))
            p3=s.find(')')
            tmp=int(s[p2+1:p3])
            l=len(str(tmp))
            (l3,m3)=(tmp*10**l,((10**l)-1)*10**(p3-p1-2))
    return adding(l1,m1,l2,m2,l3,m3)

def adding(l1,m1,l2,m2,l3,m3):
    m=nww(m1,nww(m2,m3))
    l=l1*m//m1+l2*m//m2+l3*m//m3
    nwd_lm=nwd(l,m)
    return ((l//nwd_lm),(m//nwd_lm))

def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def nww(a,b):
    return (a*b)//nwd(a,b)

s=input()
print(ulamek(s))
