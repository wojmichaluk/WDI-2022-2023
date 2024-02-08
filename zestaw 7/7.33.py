class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

#pomocnicza
def wypisz(node):
    if node!=None:
        a=node
        b=node.next
        print(a.val,end=' ')
        while b!=a:
            print(b.val,end=' ')
            b=b.next
        print()

#niestety nie wiem jak bez globala :(
def insert(r,el):
    global p
    r=p
    if r==None:
        if ord(el[-1])<ord(el[0]):
            r=Node(el)
            r.next=r
            p=r
            return True
        return False
    a=r
    b=r.next
    if ord(a.val[-1])<ord(el[0]) and ord(el[-1])<ord(b.val[0]):
        c=Node(el)
        a.next=c
        c.next=b
        p=c
        return True
    q=b.next
    while b!=a:
        if ord(b.val[-1])<ord(el[0]) and ord(el[-1])<ord(q.val[0]):
            c=Node(el)
            b.next=c
            c.next=q
            p=c
            return True
        b=b.next
        q=q.next
    return False

#testy
p=None
wypisz(p)
print(insert(p,"lasia"))
wypisz(p)
print(insert(p,"basia"))
wypisz(p)
print(insert(p,"kasia"))
wypisz(p)
print(insert(p,"marian"))
wypisz(p)
