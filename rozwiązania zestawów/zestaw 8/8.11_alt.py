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

#iteracyjnie
def insert(t,el):
    if t==None:
        t=Node()
        t.val=el
        return t
    r=t
    #while True:
    while r!=None:
        if r.val==el:
            print("Nie wstawiono elementu - duplikat.")
            return t
        elif el>r.val:
            if r.right==None:
                r.right=Node()
                r.right.val=el
                return t
            r=r.right
        else:
            if r.left==None:
                r.left=Node()
                r.left.val=el
                return t
            r=r.left
    #return t

#testy
a=None
a=insert(a,7)
a=insert(a,3)
a=insert(a,11)
a=insert(a,5)
wypisz(a)
print()
a=insert(a,4)
a=insert(a,6)
wypisz(a)
print()
a=insert(a,5)
a=insert(a,11)
wypisz(a)
