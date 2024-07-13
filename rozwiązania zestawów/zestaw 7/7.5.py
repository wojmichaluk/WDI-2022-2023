class Node:
    def __init__(self):
        self.val=None
        self.next=None

#pomocnicza
def wypisz(first):
    p=first
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    return

def split_and_merge(first):
    curr=first
    T=[Node() for _ in range(10)]
    lasts=[n for n in T]
    while curr is not None:
        nex=curr.next
        i=curr.val%10
        lasts[i].next=curr
        lasts[i]=lasts[i].next
        lasts[i].next=None
        curr=nex
    for i in range(9,-1,-1):
        T[9-i]=T[9-i].next
        if T[i]!=None:
            j=i
    k=j
    for i in range(k,9):
        if T[i+1] is not None:
            lasts[j].next=T[i+1]
            j=i+1
    return T[k:]

#testy
first=Node()
first.val=7
a=Node()
a.val=5
first.next=a
b=Node()
b.val=2
a.next=b
c=Node()
c.val=17
b.next=c
d=Node()
d.val=9
c.next=d
e=Node()
e.val=80
d.next=e
f=Node()
f.val=46
e.next=f
g=Node()
g.val=8
f.next=g
h=Node()
h.val=41
g.next=h
wypisz(first)
print()
T=split_and_merge(first)
wypisz(T[0])
