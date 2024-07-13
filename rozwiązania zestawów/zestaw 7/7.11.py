class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

def manage_key(el,zb):
    if member(el,zb):
        zb=delete(el,zb)
    else:
        zb=insert(el,zb)
    return zb

#pomocnicza
def member(el,zb):
    while zb!=None and zb.val!=el:
        zb=zb.next
    return zb!=None

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
    print("Zawartość listy: ",end='')
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()
    return

#testy
zb=Node(5)
wypisz(zb)
zb=manage_key(5,zb)
wypisz(zb)
zb=manage_key(7,zb)
wypisz(zb)
zb=manage_key(3,zb)
wypisz(zb)
zb=manage_key(7,zb)
wypisz(zb)
zb=manage_key(2,zb)
wypisz(zb)
zb=manage_key(11,zb)
wypisz(zb)
zb=manage_key(2,zb)
wypisz(zb)
