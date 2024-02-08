class Node:
    def __init__(self,val=None):
        self.val=val
        self.left=None
        self.right=None

#pomocnicza
def wypisz(p):
    if p!=None:
        print(p.val,end=' ')
        wypisz(p.right)
        wypisz(p.left)

#rekurencyjnie
def delete_all_nodes(t):
    if t!=None:
        t.left=delete_all_nodes(t.left)
        t.right=delete_all_nodes(t.right)
        t=None
    return t

#testy
a=Node(2)
a.left=Node(3)
a.right=Node(5)
a.left.right=Node(7)
a.right.left=Node(11)
a.right.left.right=Node(13)
wypisz(a)
print()
a.left=delete_all_nodes(a.left)
wypisz(a)
print()
if a!=None: wypisz(a.left)
print()
if a!=None: wypisz(a.right)
print()
if a!=None and a.left!=None: wypisz(a.left.right)
print()
if a!=None and a.right!=None: wypisz(a.right.left)
print()
if a!=None and a.right!=None and a.right.left!=None: wypisz(a.right.left.right)
print()
a=delete_all_nodes(a)
wypisz(a)
print()
if a!=None: wypisz(a.left)
print()
if a!=None: wypisz(a.right)
print()
if a!=None and a.left!=None: wypisz(a.left.right)
print()
if a!=None and a.right!=None: wypisz(a.right.left)
print()
if a!=None and a.right!=None and a.right.left!=None: wypisz(a.right.left.right)
print()
