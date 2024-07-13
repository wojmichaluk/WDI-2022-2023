class Node:
    def __init__(self,value):
        self.val=value
        self.next=None
        self.prev=None

def add(zb1,zb2):
    p1=zb1
    p2=zb2
    if p1==None and p2==None:
        return
    q1=None
    while p1!=None:
        q1=p1
        p1=p1.next
    q2=None
    while p2!=None:
        q2=p2
        p2=p2.next
    row=0
    tmp=Node(0)
    while q1!=None and q2!=None:
        v=q1.val+q2.val+row
        tmp.val=v%10
        row=v//10
        t=Node(0)
        t.next=tmp
        tmp.prev=t
        tmp=tmp.prev
        q1=q1.prev
        q2=q2.prev
    if q1==None and q2==None:
        if row==0:
            return t.next
        tmp.val=row
        return tmp
    elif q1==None:
        while q2!=None and row+q2.val>9:
            v=q2.val+row
            tmp.val=v%10
            row=v//10
            t=Node(0)
            t.next=tmp
            tmp.prev=t
            tmp=tmp.prev
            q2=q2.prev
        if q2==None:
            tmp.val=row
            return tmp
        while q2!=None:
            tmp.val=q2.val
            t=Node(0)
            t.next=tmp
            tmp.prev=t
            tmp=tmp.prev
            q2=q2.prev
    elif q2==None:
        while q1!=None and row+q1.val>9:
            v=q1.val+row
            tmp.val=v%10
            row=v//10
            t=Node(0)
            t.next=tmp
            tmp.prev=t
            tmp=tmp.prev
            q1=q1.prev
        if q1==None:
            tmp.val=row
            return tmp
        while q1!=None:
            tmp.val=q1.val
            t=Node(0)
            t.next=tmp
            tmp.prev=t
            tmp=tmp.prev
            q1=q1.prev
    return t.next

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val,end='')
        p=p.next
    print()
    return

#testy
zb1=Node(5)
zb2=Node(7)
a=Node(2)
a.prev=zb1
zb1.next=a
b=Node(4)
b.prev=a
a.next=b
c=Node(8)
c.prev=zb2
zb2.next=c
d=Node(1)
d.prev=c
c.next=d
e=Node(6)
e.prev=d
d.next=e
f=Node(5)
f.prev=e
e.next=f
wypisz(zb1)
wypisz(zb2)
zb=add(zb1,zb2)
wypisz(zb)
