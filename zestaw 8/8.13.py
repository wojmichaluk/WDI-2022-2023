class Node:
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None

#rekurencyjnie
def check_if_avl(ptr):
    if ptr==None:
        return 0
    left=check_if_avl(ptr.left)
    if left==None:
        return None
    right=check_if_avl(ptr.right)
    if right==None:
        return None
    if abs(left-right)<=1:
        return max(left,right)+1
    return None  

#testy
a=Node()
b=Node()
c=Node()
d=Node()
e=Node()
f=Node()
g=Node()
h=Node()
i=Node()
a.left=b
a.right=c
b.left=d
b.right=e
c.left=f
c.right=g
d.left=h
g.right=i
a.val=12
b.val=9
c.val=15
d.val=7
e.val=11
f.val=14
g.val=18
h.val=5
i.val=19
p=check_if_avl(a)
if p==None:
    print("To nie jest drzewo AVL")
else:
    print("To jest drzewo AVL, wysokość",p)
