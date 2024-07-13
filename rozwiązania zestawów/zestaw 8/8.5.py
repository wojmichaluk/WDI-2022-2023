class Node:
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None

#pomocnicza
def wypisz(p):
    if p!=None:
        print(p.val,end=' ')
        wypisz(p.right)
        wypisz(p.left)

#rekurencyjnie
def ile_lisci(p):
    if p==None:
        return 0
    if p.left==None and p.right==None:
        return 1
    return ile_lisci(p.left)+ile_lisci(p.right)

#testy
a=Node()
b=Node()
c=Node()
d=Node()
a.left=b
a.right=c
b.right=d
a.val=2
b.val=3
c.val=5
d.val=7
wypisz(a)
print()
print(ile_lisci(a))
e=Node()
f=Node()
b.left=e
d.right=f
e.val=11
f.val=13
wypisz(a)
print()
print(ile_lisci(a))
