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
def delete_nodes_above(t,level,cur_lev=1):
    #korzeń to poziom nr 1
    if t==None:
        return
    elif cur_lev<=level:
        t.left=delete_nodes_above(t.left,level,cur_lev+1)
        t.right=delete_nodes_above(t.right,level,cur_lev+1)
    else:
        t.left=delete_nodes_above(t.left,level,cur_lev+1)
        t.right=delete_nodes_above(t.right,level,cur_lev+1)
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
a=delete_nodes_above(a,3)
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
a=delete_nodes_above(a,2)
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
