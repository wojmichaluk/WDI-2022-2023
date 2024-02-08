class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()
    return

def funkcja(head):
    n=0
    p=head.next
    while p!=None:
        n+=1
        p=p.next
    potega=2**(n-1)
    p=head.next
    liczba=0
    while p!=None:
        liczba+=p.val*potega
        potega//=2
        p=p.next
    return liczba

#testy
head=Node(None)
a=Node(1)
head.next=a
b=Node(0)
a.next=b
c=Node(1)
b.next=c
d=Node(1)
c.next=d
e=Node(0)
d.next=e
f=Node(1)
e.next=f
wypisz(head.next)
print(funkcja(head))
