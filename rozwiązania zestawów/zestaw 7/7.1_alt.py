class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
        
def member(el,zb):
    while zb!=None and zb.val!=el:
        zb=zb.next
    return zb!=None

def member_r(el,zb):
    if zb==None:
        return False
    return zb.val==el or member_r(el,zb.next)

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

def insert_r(el,zb):
    first=zb
    def rek(el,zb):
        nonlocal first
        if zb==None or zb!=None and zb.val>el:
            p=Node(el)
            p.next=zb
            return p
        if zb!=None and zb.val<el:
            if zb.next!=None and zb.next.val>el:
                p=Node(el)
                p.next=zb.next
                zb.next=p
                return first
            if zb.next==None:
                p=Node(el)
                zb.next=p
                return first
            return rek(el,zb.next)
        return first
    first=rek(el,first)
    return first

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

#testy
zb=Node(5)
zb=delete(5,zb)
zb=delete(7,zb)
wypisz(zb)
"""zb=insert(3,zb)
zb=insert(7,zb)
zb=insert(2,zb)
zb=insert(17,zb)
zb=insert(7,zb)
zb=insert(13,zb)
zb=insert(11,zb)"""
zb=insert_r(3,zb)
zb=insert_r(3,zb)
zb=insert_r(7,zb)
zb=insert_r(2,zb)
zb=insert_r(17,zb)
zb=insert_r(7,zb)
zb=insert_r(13,zb)
zb=insert_r(11,zb)
zb=insert_r(3,zb)
zb=delete(2,zb)
wypisz(zb)
print(member(7,zb))
print(member(17,zb))
print(member(9,zb))
print(member_r(7,zb))
print(member_r(17,zb))
print(member_r(9,zb))
