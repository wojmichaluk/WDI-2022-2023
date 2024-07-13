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
def height(t):
    if t==None:
        return 0
    return 1+max(height(t.left),height(t.right))

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
print(height(a))
e=Node()
f=Node()
d.left=e
e.right=f
e.val=11
f.val=13
wypisz(a)
print()
print(height(a))
