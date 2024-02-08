class Node:
    def __init__(self):
        self.next=None

def hasCycle(head):
    if head==None:
        return False
    fast=head
    slow=head
    while fast.next!=None and fast.next.next!=None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return True
    return False

#pomocnicza
def wypisz(zb):
    i=0
    p=zb
    while p!=None and i<10:
        print("teścik",end=' ')
        p=p.next
        i+=1
    print()
    return

#testy
head=Node()
a=Node()
head.next=a
b=Node()
a.next=b
c=Node()
b.next=c
d=Node()
c.next=d
e=Node()
d.next=e
e.next=b
#wypisz(head)
print(hasCycle(head))
e.next=None
print(hasCycle(head))
