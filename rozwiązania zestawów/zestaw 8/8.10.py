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
def is_in_BST(t,el):
    if t!=None:
        if t.val==el:
            return True
        elif el>t.val:
            return is_in_BST(t.right,el)
        return is_in_BST(t.left,el)
    return False

#testy
a=Node()
b=Node()
c=Node()
d=Node()
a.left=b
a.right=c
b.right=d
a.val=7
b.val=3
c.val=11
d.val=5
wypisz(a)
print()
print(is_in_BST(a,6))
print(is_in_BST(a,5))
e=Node()
f=Node()
d.left=e
d.right=f
e.val=4
f.val=6
wypisz(a)
print()
print(is_in_BST(a,6))
print(is_in_BST(a,13))
