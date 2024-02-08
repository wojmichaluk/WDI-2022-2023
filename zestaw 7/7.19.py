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

def only_unique(zb):
    p=zb
    q=None
    count=0
    while p!=None:
        if q!=None and q.val==p.val:
            count+=1
            q.next=p.next
            p=p.next
        else:
            q=p
            p=p.next
    return count

#testy
zb=Node(2)
a=Node(3)
zb.next=a
b=Node(5)
a.next=b
c=Node(5)
b.next=c
wypisz(zb)
A=only_unique(zb)
print("Usunięto elementów:",A)
wypisz(zb)
d=Node(6)
b.next=d
e=Node(6)
d.next=e
f=Node(15)
e.next=f
g=Node(15)
f.next=g
wypisz(zb)
B=only_unique(zb)
print("Usunięto elementów:",B)
wypisz(zb)
