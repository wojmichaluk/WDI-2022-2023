class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None

def odd_one_in_binary(el):
    count=0
    while el>0:
        count+=el%2
        el//=2
    return count%2==1

#wersja z wartownikiem        
def usun(head):
    p=head
    i=head
    while i.next!=None:
        i=i.next
        if not odd_one_in_binary(i.val):
            i.prev=p
            p.next=i
            p=p.next
    p.next=None
    return

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        if p.val!=None:
            print(p.val,end=' ')
        p=p.next
    print()
    return

#testy
head=Node(None)
a=Node(5)
head.next=a
a.prev=head
b=Node(19)
a.next=b
b.prev=a
c=Node(52)
b.next=c
c.prev=b
d=Node(7)
c.next=d
d.prev=c
wypisz(head)
usun(head)
wypisz(head)
