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

def merge(first):
    p=first
    while p!=None:
        l=p
        q=p.next
        while q!=None:
            new=scal(p.val,q.val)
            if new:
                p.val=new
                l.next=q.next
            else:
                l=q
            q=q.next
        p=p.next
    return first

def scal(k1,k2):
    if k1[1]>=k2[0] and k2[1]>=k1[0]:
        return (min(k1[0],k2[0]),max(k1[1],k2[1]))
    return

#testy
a=Node((15,19))
b=Node((2,5))
a.next=b
c=Node((7,11))
b.next=c
d=Node((8,12))
c.next=d
e=Node((5,6))
d.next=e
f=Node((13,17))
e.next=f
wypisz(a)
a=merge(a)
wypisz(a)
