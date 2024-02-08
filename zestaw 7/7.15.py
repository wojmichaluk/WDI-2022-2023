class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

def delete_trojkowy(zb):
    p=zb
    while p!=None:
        if trojkowy(p.val):
            #zakładam, że elementy się nie powtarzają
            zb=delete(p.val,zb)
        p=p.next
    return zb

def delete(el,zb):
    r=zb
    q=None
    while r!=None and r.val!=el:
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
        print(p.val,end=' ')
        p=p.next
    print()
    return

#pomocnicza
def trojkowy(el):
    liczba_jedynek=liczba_dwojek=0
    while el>0:
        if el%3==1:
            liczba_jedynek+=1
        elif el%3==2:
            liczba_dwojek+=1
        el//=3
    return liczba_jedynek>liczba_dwojek

#testy
zb=Node(3)
a=Node(81)
zb.next=a
b=Node(8)
a.next=b
wypisz(zb)
zb=delete_trojkowy(zb)
wypisz(zb)
c=Node(28)
b.next=c
d=Node(55)
c.next=d
e=Node(9)
d.next=e
f=Node(18)
e.next=f
wypisz(zb)
zb=delete_trojkowy(zb)
wypisz(zb)
