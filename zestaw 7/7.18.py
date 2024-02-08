class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()
    return

#pomocnicza
def already_in_list(beg,end):
    p=beg
    k=end
    while p!=k:
        if p.val==k.val:
            return True
        p=p.next
    return False

def only_unique(zb):
    p=zb
    q=None
    while p!=None:
        if already_in_list(zb,p):
            q.next=p.next
            p=p.next
        else:
            q=p
            p=p.next
    return zb

#testy
zb=Node(5)
a=Node(5)
zb.next=a
b=Node(6)
a.next=b
c=Node(2)
b.next=c
wypisz(zb)
zb=only_unique(zb)
wypisz(zb)
d=Node(35)
c.next=d
e=Node(6)
d.next=e
f=Node(2)
e.next=f
g=Node(15)
f.next=g
wypisz(zb)
zb=only_unique(zb)
wypisz(zb)
