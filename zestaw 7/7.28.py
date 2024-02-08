class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None

def usun_powtorzenia(p1,p2):
    #p1,p2 to wartowniki
    r2=p2.next
    q2=p2
    count=0
    while r2!=None:
        if deleted(p1,r2.val):
            q2.next=r2.next
            count+=1
        else:
            q2=r2
        r2=r2.next
    return count

def deleted(p,val):
    q=p
    r=p.next
    while r!=None and r.val<val:
        q=r
        r=r.next
    if r==None:
        return False
    elif r.val>val:
        return False
    else:
        q.next=r.next
        return True

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
a=Node(3)
wart2.next=a
b=Node(6)
a.next=b
c=Node(5)
b.next=c
d=Node(1)
c.next=d
e=Node(1)
wart1.next=e
f=Node(3)
e.next=f
g=Node(4)
f.next=g
h=Node(7)
g.next=h
wypisz(wart1.next)
wypisz(wart2.next)
print(usun_powtorzenia(wart1,wart2))
wypisz(wart1.next)
wypisz(wart2.next)
