class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def member(p,el):
    while p!=None and p.val!=el:
        p=p.next
    return p!=None

def wypisz(p):
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()

def iloczyn(z1,z2,z3):
    p1=z1
    p2=z2
    flag=True
    p=None
    while p1!=None:
        if member(p2,p1.val):
            if flag:
                p=Node(p1.val)
                r=p
                flag=False
            else:
                r.next=Node(p1.val)
                r=r.next
        p1=p1.next
    s=None
    p3=z3
    flag=True
    while p!=None:
        if member(p3,p.val):
            if flag:
                s=Node(p.val)
                t=s
                flag=False
            else:
                t.next=Node(p.val)
                t=t.next
        p=p.next
    return s

#testy
z1=Node(1)
a=Node(3)
z1.next=a
b=Node(4)
a.next=b
c=Node(5)
b.next=c
z2=Node(2)
d=Node(3)
z2.next=d
e=Node(5)
d.next=e
f=Node(7)
e.next=f
z3=Node(3)
g=Node(4)
z3.next=g
h=Node(5)
g.next=h
i=Node(7)
h.next=i
wypisz(z1)
wypisz(z2)
wypisz(z3)
z=iloczyn(z1,z2,z3)
wypisz(z)
