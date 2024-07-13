class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

def delete(zb):
    r=zb
    if r==None:
        print("Pusta lista - nie ma co usuwać!")
        return zb
    q=None
    while r.next!=None:
        q=r
        r=r.next  
    if q==None:
        return None
    q.next=None
    return zb

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val)
        p=p.next
    return

#testy
zb=Node(5)
wypisz(zb)
zb=delete(zb)
zb=delete(zb)
wypisz(zb)
zb=Node(5)
a=Node(7)
zb.next=a
b=Node(8)
a.next=b
wypisz(zb)
zb=delete(zb)
wypisz(zb)
c=Node(13)
a.next=c
d=Node(18)
c.next=d
e=Node(27)
d.next=e
f=Node(38)
e.next=f
wypisz(zb)
zb=delete(zb)
zb=delete(zb)
wypisz(zb)
