class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

def insert(el,zb):
    r=zb
    if r==None:
        return Node(el)
    q=None
    while r!=None:
        q=r
        r=r.next
    p=Node(el)
    q.next=p
    return zb

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val)
        p=p.next
    return

#testy
zb=insert(5,None)
wypisz(zb)
print()
zb=insert(2,zb)
zb=insert(11,zb)
zb=insert(7,zb)
wypisz(zb)
print()
zb=insert(23,zb)
zb=insert(3,zb)
zb=insert(13,zb)
wypisz(zb)
