class Node:
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None

#rekurencyjnie v1
def wypisz(p):
    if p!=None:
        print(p.val,end=' ')
        wypisz(p.right)
        wypisz(p.left)

#rekurencyjnie v2
def wypisz2(p):
    if p!=None:
        print(p.val,end=' ')
        if p.right!=None:
            wypisz2(p.right)
        if p.left!=None:
            wypisz2(p.left)

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
wypisz2(a)
print()
