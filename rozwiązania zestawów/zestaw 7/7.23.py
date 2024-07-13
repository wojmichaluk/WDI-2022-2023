class Node:
    def __init__(self):
        self.next=None

def cycle_length(head):
    count=0
    fast=head
    slow=head
    while True:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            break
    fast=fast.next.next
    slow=slow.next
    count+=1
    while fast!=slow:
        count+=1
        fast=fast.next.next
        slow=slow.next
    return count

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
print(cycle_length(head))
e.next=d
print(cycle_length(head))
