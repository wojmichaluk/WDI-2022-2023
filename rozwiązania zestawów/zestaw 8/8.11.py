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
def insert_BST(t,el):
    if t==None:
        t=Node()
        t.val=el
        return t
    if t.val==el:
        return t
    if t.val>el:
        t.left=insert_BST(t.left,el)
    else:
        t.right=insert_BST(t.right,el)
    return t

#testy
a=None
a=insert_BST(a,7)
a=insert_BST(a,3)
a=insert_BST(a,11)
a=insert_BST(a,5)
wypisz(a)
print()
a=insert_BST(a,4)
a=insert_BST(a,6)
wypisz(a)
print()
a=insert_BST(a,5)
a=insert_BST(a,11)
wypisz(a)
