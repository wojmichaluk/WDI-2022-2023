class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

#"odwraca" elementy
def move_osemkowy(zb):
    p=zb
    while p!=None:
        if osemkowy(p.val):
            r=Node(p.val)
            zb=delete(p.val,zb)
            r.next=zb
            zb=r
        p=p.next
    return zb

#zachowuje kolejność
def move_osemkowy2(zb):
    p=zb
    i=0
    while p!=None:
        if osemkowy(p.val):
            r=Node(p.val)
            zb=delete(p.val,zb)
            s=zb
            t=None
            for j in range(i):
                t=s
                s=s.next
            if t==None:
                r.next=zb
                zb=r
            else:
                t.next=r
                r.next=s
            i+=1
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
def osemkowy(el):
    liczba_piatek=0
    while el>0:
        if el%8==5:
            liczba_piatek+=1
        el//=8
    return liczba_piatek%2==0

#testy
zb=Node(45)
a=Node(29)
zb.next=a
b=Node(367)
a.next=b
wypisz(zb)
zb=move_osemkowy(zb)
#zb=move_osemkowy2(zb)
wypisz(zb)
c=Node(47)
a.next=c
d=Node(17)
c.next=d
e=Node(21)
d.next=e
f=Node(62)
e.next=f
wypisz(zb)
zb=move_osemkowy(zb)
#zb=move_osemkowy2(zb)
wypisz(zb)
