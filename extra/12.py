class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def wypisz(p):
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()

#dla listy bez powtarzających się wartości
def sorting_llist(head):
    a=Node()
    h=a
    s=head
    min_val=max_val=head.val
    min_node=head
    while s!=None:
        if s.val<=min_val:
            min_val=s.val
            min_node=s
        if s.val>=max_val:
            max_val=s.val
        s=s.next
    b=Node(min_val)
    a.next=b
    a=a.next
    last_min_node=min_node
    min_node=head
    last_min_val=min_val
    min_val=head.val
    s=head.next
    while s!=None:
        r=head
        min_val=max_val
        while r!=None:
            if r!=last_min_node and r.val>=last_min_val and r.val<=min_val:
                min_val=r.val
                min_node=r
            r=r.next
        last_min_node=min_node
        last_min_val=min_val
        b=Node(min_val)
        a.next=b
        a=a.next
        s=s.next
    return h.next

#testy
head=Node(3)
a=Node(6)
head.next=a
b=Node(4)
a.next=b
c=Node(7)
b.next=c
d=Node(1)
c.next=d
wypisz(head)
#h=sorting_llist(head)
head=sorting_llist(head)
#wypisz(h)
wypisz(head) 
