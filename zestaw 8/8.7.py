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
def nodes_with_one_child(t):
    if t==None:
        return 0
    a=0
    if t.left==None and t.right!=None or t.left!=None and t.right==None:
        a=1
    return a+nodes_with_one_child(t.left)+nodes_with_one_child(t.right)

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
print(nodes_with_one_child(a))
e=Node()
f=Node()
d.left=e
e.right=f
e.val=11
f.val=13
wypisz(a)
print()
print(nodes_with_one_child(a))
