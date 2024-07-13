class Node:
    def __init__(self):
        self.next=None
        
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
e.next=head
print(before_cycle_length(head))
e.next=d
print(before_cycle_length(head))
