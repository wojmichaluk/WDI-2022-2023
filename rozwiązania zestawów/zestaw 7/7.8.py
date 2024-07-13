class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

def delete_every_second(zb):
    zb=zb.next
    r=zb
    q=None
    i=1
    while r!=None:
        if i%2==0:
            q.next=r.next
        q=r
        r=r.next
        i+=1
    return zb

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val)
        p=p.next
    return

#testy
zb=Node(2)
a=Node(3)
zb.next=a
wypisz(zb)
print()
zb=delete_every_second(zb)
wypisz(zb)
print()
a=Node(5)
zb.next=a
b=Node(7)
a.next=b
c=Node(11)
b.next=c
d=Node(13)
c.next=d
e=Node(17)
d.next=e
f=Node(19)
e.next=f
wypisz(zb)
print()
zb=delete_every_second(zb)
wypisz(zb)
