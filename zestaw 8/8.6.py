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
def nodes_leveln(t,level):
    #korzeń to poziom nr 1
    if t==None:
        return 0
    elif level==1:
        return 1
    return nodes_leveln(t.left,level-1)+nodes_leveln(t.right,level-1)

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
print(nodes_leveln(a,1))
print(nodes_leveln(a,2))
print(nodes_leveln(a,3))
print(nodes_leveln(a,4))
print(nodes_leveln(a,5))
e=Node()
f=Node()
d.left=e
e.right=f
e.val=11
f.val=13
wypisz(a)
print()
print(nodes_leveln(a,1))
print(nodes_leveln(a,2))
print(nodes_leveln(a,3))
print(nodes_leveln(a,4))
print(nodes_leveln(a,5))
