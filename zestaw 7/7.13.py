class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
        self.prev=None

def delete_smaller(zb):
    p=zb
    if p==None:
        print("Nie ma co usuwać - pusta lista")
        return zb
    q=None
    while p!=None:
        q=p
        p=p.next
    r=q.prev
    while r!=None:
        if q.val<r.val:
            #przy założeniu, że elementy w liście się nie powtarzają
            zb=delete(q.val,zb)
        q=r
        r=r.prev
    return zb

def delete(el,zb):
    r=zb
    q=None
    while r.val!=el:
        q=r
        r=r.next  
    q.next=r.next
    if r.next!=None:
        r.next.prev=q
    return zb

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()
    return

def delete_rek(zb):
    if zb.next is None:
        return
    else:
        delete_rek(zb.next)
        if zb.next.val<zb.val:
            zb.next=zb.next.next

#testy
zb=Node(5)
a=Node(3)
zb.next=a
a.prev=zb
b=Node(7)
a.next=b
b.prev=a
c=Node(1)
b.next=c
c.prev=b
wypisz(zb)
#zb=delete_smaller(zb)
delete_rek(zb)
wypisz(zb)
d=Node(8)
b.next=d
d.prev=b
e=Node(1)
d.next=e
e.prev=d
f=Node(17)
e.next=f
f.prev=e
g=Node(1)
f.next=g
g.prev=f
wypisz(zb)
#zb=delete_smaller(zb)
delete_rek(zb)
wypisz(zb)
