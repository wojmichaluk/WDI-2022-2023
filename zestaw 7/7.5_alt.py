class Node:
    def __init__(self):
        self.val=None
        self.next=None

def dziel(p):
    Tp=[None for _ in range(10)]
    Tk=[None for _ in range(10)]
    while p!=None:
        i=p.val%10
        if Tp[i]==None:
            Tp[i]=p
            Tk[i]=p
        else:
            Tk[i].next=p
            Tk[i]=p
        p=p.next
    res=None
    for i in range(9,-1,-1):
        if Tp[i]!=None:
            Tk[i].next=res
            res=Tp[i]
    return res

#pomocnicza
def wypisz(first):
    p=first
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    return

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
fir=dziel(first)
wypisz(fir)
