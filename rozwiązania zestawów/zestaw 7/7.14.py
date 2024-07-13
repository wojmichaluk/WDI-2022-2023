class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()
    return

def delete(zb):
    #wersja z wartownikiem
    if zb.next is None or zb.next.next is None:
        return
    else:
        if zb.next.val!=0 and zb.next.next.val%zb.next.val==0:
            zb.next=zb.next.next
            delete(zb)
        else:
            delete(zb.next)

#testy
zb=Node(None)
a=Node(3)
zb.next=a
b=Node(6)
a.next=b
c=Node(2)
b.next=c
wypisz(zb.next)
delete(zb)
wypisz(zb.next)
d=Node(8)
c.next=d
e=Node(16)
d.next=e
f=Node(32)
e.next=f
g=Node(1)
f.next=g
wypisz(zb.next)
delete(zb)
wypisz(zb.next)
