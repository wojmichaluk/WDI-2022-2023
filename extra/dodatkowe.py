class Node:
    def __init__(self,val=None):
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

def funkcja(T):
    n=len(T)
    G=[None for _ in range(n)]
    Gend=[None for _ in range(n)]
    for i in range(n):
        nn=Node()
        G[i]=nn
        Gend[i]=nn
    for i in range(n):
        p=T[i].next
        while p!=None:
            Gend[p.val-1].next=p
            Gend[p.val-1]=p
            p=p.next
    for i in range(n):
        Gend[i].next=None
        T[i].next=G[i].next

#testy
T=[None for _ in range(3)]
for i in range(3):
    nn=Node()
    T[i]=nn
a=Node(1)
b=Node(3)
a.next=b
c=Node(2)
b.next=c
d=Node(3)
c.next=d
e=Node(2)
f=Node(1)
e.next=f
g=Node(3)
f.next=g
h=Node(1)
g.next=h
i=Node(3)
j=Node(2)
i.next=j
k=Node(1)
j.next=k
l=Node(1)
k.next=l
T[0].next=a
T[1].next=e
T[2].next=i
wypisz(T[0].next)
wypisz(T[1].next)
wypisz(T[2].next)
funkcja(T)
wypisz(T[0].next)
wypisz(T[1].next)
wypisz(T[2].next)
