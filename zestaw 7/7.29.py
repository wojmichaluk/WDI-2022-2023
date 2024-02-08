class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def usun_niepowtorzenia(p1,p2):
    #p1,p2 to wartowniki
    r2=p2.next
    q2=p2
    count=0
    while r2!=None:
        if nonmember(p1,r2.val):
            q2.next=r2.next
            count+=1
        else:
            q2=r2
        r2=r2.next
    r1=p1.next
    q1=p1
    while r1!=None:
        if nonmember(p2,r1.val):
            q1.next=r1.next
            count+=1
        else:
            q1=r1
        r1=r1.next
    return count

def nonmember(p,val):
    q=p
    r=p.next
    while r!=None and r.val<val:
        q=r
        r=r.next
    if r==None or r.val>val:
        return True
    else:
        return False

#pomocnicza
def wypisz(p):
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()
    return

#testy
wart1=Node()
wart2=Node()
a=Node(1)
wart2.next=a
b=Node(4)
a.next=b
c=Node(6)
b.next=c
d=Node(7)
c.next=d
e=Node(2)
wart1.next=e
f=Node(3)
e.next=f
g=Node(5)
f.next=g
h=Node(8)
g.next=h
wypisz(wart1.next)
wypisz(wart2.next)
print(usun_niepowtorzenia(wart1,wart2))
wypisz(wart1.next)
wypisz(wart2.next)
