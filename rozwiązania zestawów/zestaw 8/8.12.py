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
def check_if_BST(t,minval=0,maxval=0):
    if t==None:
        return True
    a=b=True
    if t.left!=None:
        if t.val>t.left.val and (maxval==0 or t.left.val<maxval) and (minval==0 or t.left.val>minval):
            a=check_if_BST(t.left,minval,t.val)
        else:
            return False
    if t.right!=None:
        if t.val<t.right.val and (minval==0 or t.right.val>minval) and (maxval==0 or t.right.val<maxval):
            b=check_if_BST(t.right,t.val,maxval)
        else:
            return False
    return a and b

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
print(check_if_BST(a))
e=Node()
f=Node()
d.left=e
d.right=f
e.val=4
f.val=6
wypisz(a)
print()
print(check_if_BST(a))
