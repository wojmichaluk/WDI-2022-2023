class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

#pomocnicza
def insert(el,zb):
    r=zb
    q=None
    while r!=None and r.val<el:
        q=r
        r=r.next
    if r!=None and r.val==el:
        return zb
    p=Node(el)
    p.next=r
    if q!=None:
        q.next=p
    else:
        zb=p
    return zb

#pomocnicza
def delete(el,zb):
    r=zb
    q=None
    while r!=None and r.val<el:
        q=r
        r=r.next  
    if r!=None and r.val==el:
        if q==None:
            return zb.next
        q.next=r.next
    return zb

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val)
        p=p.next
    return

def reverse(zb):
    r=None
    p=zb
    if p!=None:
        r=Node(p.val)
        p=p.next
    while p!=None:
        q=Node(p.val)
        q.next=r
        r=q
        p=p.next
    return r

#testy
zb=Node(5)
#zb=delete(5,zb)
wypisz(zb)
tmp=reverse(zb)
wypisz(tmp)
zb=insert(3,zb)
zb=insert(7,zb)
zb=insert(2,zb)
zb=insert(17,zb)
zb=insert(7,zb)
zb=insert(13,zb)
zb=insert(11,zb)
wypisz(zb)
zb=reverse(zb)
wypisz(zb)
