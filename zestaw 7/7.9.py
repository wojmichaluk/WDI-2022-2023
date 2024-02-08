class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
        self.prev=None

def add_one(zb):
    p=zb
    if p==None:
        return zb
    q=None
    while p!=None:
        q=p
        p=p.next
    q.val+=1
    r=q
    while r.val//10>0:
        r.val%=10
        t=r
        r=r.prev
        if r==None:
            break
        r.val+=1
    if r!=None:
        return zb
    n=Node(1)
    n.next=t
    t.prev=n
    return n

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val,end='')
        p=p.next
    print()
    return

#testy
zb=Node(2)
a=Node(9)
a.prev=zb
zb.next=a
b=Node(9)
b.prev=a
a.next=b
c=Node(8)
c.prev=b
b.next=c
wypisz(zb)
zb=add_one(zb)
wypisz(zb)
zb=add_one(zb)
wypisz(zb)
