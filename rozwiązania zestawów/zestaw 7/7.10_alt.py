class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val,end='')
        p=p.next
    print()
    return

#pomocnicza
def uzupelnij(a,b):
    p1=a
    p2=b
    l1=l2=0
    while p1!=None:
        l1+=1
        p1=p1.next
    while p2!=None:
        l2+=1
        p2=p2.next
    if l2==l1:
        return a,b
    elif l1>l2:
        while l1>l2:
            l1-=1
            tmp=Node(0)
            tmp.next=b
            b=tmp
    else:
        while l2>l1:
            l2-=1
            tmp=Node(0)
            tmp.next=a
            a=tmp
    return a,b

def add(a,b):
    def rek(p1,p2):
        if p1.next==None:
            value=(p1.val+p2.val)%10
            h=Node(value)
            return h
        else:
            g=Node()
            con=rek(p1.next,p2.next)
            g.next=con
            g.val=p1.val+p2.val+(p1.next.val+p2.next.val)//10
            g.val%=10
            return g
    c=rek(a,b)
    if c.val<a.val or c.val<b.val:
        d=Node(1)
        d.next=c
        return d
    return c

#testy
zb1=Node(5)
zb2=Node(4)
a=Node(2)
zb1.next=a
b=Node(4)
a.next=b
c=Node(8)
b.next=c
d=Node(1)
c.next=d
e=Node(6)
zb2.next=e
f=Node(5)
e.next=f
zb1,zb2=uzupelnij(zb1,zb2)
wypisz(zb1)
wypisz(zb2)
zb=add(zb1,zb2)
wypisz(zb)
