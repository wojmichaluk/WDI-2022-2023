class Node:
    def __init__(self,val):
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

def delete_longest(zb):
    def wew(zb):
        #wersja z wartownikiem
        q=zb.next
        if q==None or q.next==None:
            zb.next=None
            return
        p=q.next
        curr=1
        longest=1
        counter_longest=2
        while p!=None:
            if p.val>q.val:
                curr+=1
            else:
                if curr==longest:
                    counter_longest+=1
                curr=1
            if curr>longest:
                longest=curr
                counter_longest=0
            q=p
            p=p.next
        if curr==longest:
            counter_longest+=1
        return longest,counter_longest
    a=wew(zb)
    if a==None:
        return
    elif a[1]>1:
        return
    else:
        prev=zb
        q=zb.next
        p=q.next
        curr_len=1
        while p!=None:
            while p!=None and p.val>q.val:
                q=p
                p=p.next
                curr_len+=1
            if curr_len==a[0]:
                prev.next=p
                break
            curr_len=1
            q=p
            p=p.next
            while prev.next!=q:
                prev=prev.next
        return

#testy
zb=Node(None)
a=Node(50)
zb.next=a
b=Node(73)
a.next=b
c=Node(109)
b.next=c
d=Node(1000)
c.next=d
e=Node(15)
d.next=e
f=Node(1900)
e.next=f
wypisz(zb.next)
delete_longest(zb)
wypisz(zb.next)
