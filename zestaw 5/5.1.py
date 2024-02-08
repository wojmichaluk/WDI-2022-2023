def addition(*args):
    (l1,m1)=args[0]
    (l2,m2)=args[1]
    m=nww(m1,m2)
    l=l1*(m//m1)+l2*(m//m2)
    return shorten((l,m))

def sub(*args):
    (l1,m1)=args[0]
    (l2,m2)=args[1]
    return addition((l1,m1),(l2*(-1),m2))

def multi(*args):
    (l1,m1)=args[0]
    (l2,m2)=args[1]
    l=l1*l2
    m=m1*m2
    return shorten((l,m))

def division(*args):
    (l1,m1)=args[0]
    (l2,m2)=args[1]
    return multi((l1,m1),(m2,l2))

def shorten(*args):
    (l,m)=args[0]
    return l//nwd(l,m),m//nwd(l,m)

def power(*args):
    (l1,m1)=args[0]
    (l2,m2)=args[1]
    return(l1/m1)**(l2/m2)

def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def nww(a,b):
    return (a*b)//nwd(a,b)

l1,m1=input().split(',')
l1,m1=int(l1),int(m1)
l2,m2=input().split(',')
l2,m2=int(l2),int(m2)
print(addition((l1,m1),(l2,m2)))
print(sub((l1,m1),(l2,m2)))
print(multi((l1,m1),(l2,m2)))
print(division((l1,m1),(l2,m2)))
print(shorten((l1,m1)))
print(power((l1,m1),(l2,m2)))
