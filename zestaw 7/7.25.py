class Node:
    def __init__(self,val):
        self.next=None
        self.val=val #do testów

#pomocnicza       
def before_cycle_length(head):
    fast=head
    slow=head
    while True:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            break
    count=0
    fast=head
    while fast!=slow:
        fast=fast.next
        slow=slow.next
        count+=1
    return count

def get_first_before_cycle(head):
    l=before_cycle_length(head)
    l-=1
    if l<0:
        return None
    temp=head
    while l>0:
        l-=1
        temp=temp.next
    return temp

#testy
head=Node(1)
a=Node(2)
head.next=a
b=Node(3)
a.next=b
c=Node(4)
b.next=c
d=Node(5)
c.next=d
e=Node(6)
d.next=e
e.next=b
f=get_first_before_cycle(head)
if f!=None:
    print(f.val)
e.next=d
f=get_first_before_cycle(head)
if f!=None:
    print(f.val)
