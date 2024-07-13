class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def wypisz(p):
    if p!=None:
        print(p.val)
        wypisz(p.right)
        wypisz(p.left)

def wypisz2(p):
    if p!=None:
        print(p.val)
        if p.right!=None:
            wypisz2(p.right)
        if p.left!=None:
            wypisz2(p.left)

def leniwy_ojciec(p):
    if p==None:
        return 0
    return leniwy_ojciec(p.left)+leniwy_ojciec(p.right)+1

def ile_lisci(p):
    if p==None:
        return 0
    if p.left==None and p.right==None:
        return 1
    return ile_lisci(p.left)+ile_lisci(p.right)

#testy
a=Tree(2)
b=Tree(3)
c=Tree(5)
d=Tree(7)
a.left=b
a.right=c
b.right=d
wypisz(a)
wypisz2(a)
print(leniwy_ojciec(a))
print(ile_lisci(a))

        
