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
def member(p,el):
    if p!=None:
        return p.val==el or member(p.left,el) or member(p.right,el)
    return False

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
print(member(a,2))
print(member(a,8))
print(member(a,7))
print(member(a,11))
