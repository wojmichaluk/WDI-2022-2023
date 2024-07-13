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

#zakładam, że względna kolejność jest taka sama
def includes(zb1,zb2):
    p1=zb1
    p2=zb2
    if p1==None or p2==None:
        return True
    while p1!=None:
        a=p2.val
        while p1!=None and p1.val!=a:
            p1=p1.next
        if p1==None:
            break
        p2=p2.next
        if p2==None:
            return True
    p1=zb1
    p2=zb2
    while p2!=None:
        a=p1.val
        while p2!=None and p2.val!=a:
            p2=p2.next
        if p2==None:
            break
        p1=p1.next
        if p1==None:
            return True
    return False

#testy
zb1=Node(5)
a=Node(15)
zb1.next=a
b=Node(25)
a.next=b
zb2=Node(5)
c=Node(10)
zb2.next=c
d=Node(15)
c.next=d
e=Node(20)
d.next=e
f=Node(25)
e.next=f
wypisz(zb1)
wypisz(zb2)
print(includes(zb1,zb2))
