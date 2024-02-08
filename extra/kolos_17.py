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

def fun(A,B):
    currA=A
    while currA!=None:
        currB=B
        while currB!=None and currB.next!=currA.next:
            currB=currB.next
        if currB!=None:
            break
        else:
            currA=currA.next
    to_copy=None
    cnt=0
    if currA!=None:
        to_copy=currA.next
    while to_copy!=None:
        cnt+=1
        currB.next=Node(to_copy.val)
        currB=currB.next
        to_copy=to_copy.next
    return cnt

#testy
a=Node(5)
b=Node(11)
a.next=b
c=Node(3)
b.next=c
d=Node(2)
c.next=d
e=Node(13)
f=Node(7)
e.next=f
g=Node(17)
f.next=g
g.next=c
print(fun(a,e))
wypisz(a)
wypisz(e)
