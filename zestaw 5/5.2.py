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

def solve(*args):
    (la1,ma1,lb1,mb1,lc1,mc1)=args[0]
    (la2,ma2,lb2,mb2,lc2,mc2)=args[1]
    one=nww(ma1,nww(mb1,mc1))
    ma1=mb1=mc1=one
    la1*=one//ma1
    lb1*=one//mb1
    lc1*=one//mc1
    two=nww(ma2,nww(mb2,mc2))
    ma2=mb2=mc2=two
    la2*=two//ma2
    lb2*=two//mb2
    lc2*=two//mc2
    (l1,m1)=(la1,ma1)
    (la1,ma1)=multi((la1,ma1),(la2,ma2))
    (lb1,mb1)=multi((lb1,mb1),(la2,ma2))
    (lc1,mc1)=multi((lc1,mc1),(la2,ma2))
    (la2,ma2)=multi((la2,ma2),(l1,m1))
    (lb2,mb2)=multi((lb2,mb2),(l1,m1))
    (lc2,mc2)=multi((lc2,mc2),(l1,m1))
    lb,mb=sub((lb1,mb1),(lb2,mb2))
    lc,mc=sub((lc1,mc1),(lc2,mc2))
    ly,my=division((lc,mc),(lb,mb))
    lleft,mleft=sub((lc1,mc1),multi((lb1,mb1),(ly,my)))
    lx,mx=division((lleft,mleft),(la1,ma1))
    return (lx,mx),(ly,my)
    
la1,ma1,lb1,mb1,lc1,mc1=input().split(',')
la1,ma1,lb1,mb1,lc1,mc1=int(la1),int(ma1),int(lb1),int(mb1),int(lc1),int(mc1)
la2,ma2,lb2,mb2,lc2,mc2=input().split(',')
la2,ma2,lb2,mb2,lc2,mc2=int(la2),int(ma2),int(lb2),int(mb2),int(lc2),int(mc2)
print(solve((la1,ma1,lb1,mb1,lc1,mc1),(la2,ma2,lb2,mb2,lc2,mc2)))
