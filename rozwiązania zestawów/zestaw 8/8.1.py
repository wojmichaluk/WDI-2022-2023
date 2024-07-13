class Node:
    def __init__(self):
        self.val=None
        self.left=None
        self.right=None

#iteracyjnie
def wypisz(ptr):
    stos=[]
    stos.append(ptr)
    while len(stos)>0:
        cur=stos.pop()
        if cur!=None:
            print(cur.val,end=' ')
            stos.append(cur.left)
            stos.append(cur.right)

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
