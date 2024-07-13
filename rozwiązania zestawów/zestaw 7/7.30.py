class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def scal(p1,p2):
    r1=p1
    r2=p2
    while r2!=None:
        r1=insert(r1,r2.val)
        r2=r2.next
    return r1

def insert(p,val):
    q=None
    r=p
    while r!=None and r.val<val:
        q=r
        r=r.next
    if r==None:
        q.next=Node(val)
        return p
    elif r.val==val:
        return p
    elif q==None:
        t=Node(val)
        t.next=r
        return t
    else:
        t=Node(val)
        q.next=t
        t.next=r
        return p

#pomocnicza
def wypisz(p):
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()
    return

#testy
a=Node(2)
b=Node(3)
a.next=b
c=Node(5)
b.next=c
d=Node(7)
c.next=d
e=Node(11)
d.next=e
f=Node(8)
g=Node(2)
f.next=g
h=Node(7)
g.next=h
i=Node(4)
h.next=i
wypisz(a)
wypisz(f)
a=scal(a,f)
wypisz(a)
#wypisz(f)
