class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def rozdziel(Dhead,Whead1,Whead2):
    count=0
    p1=Whead1
    p2=Whead2
    i=Dhead
    #wersja z wartownikiem
    while i.next!=None:
        i=i.next
        if parz_dod(i.val):
            p1.next=i
            p1=p1.next
        elif niep_ujemne(i.val):
            p2.next=i
            p2=p2.next
        else:
            count+=1
    p1.next=None
    p2.next=None
    return count

def parz_dod(n):
    return n>0 and n%2==0

def niep_ujemne(n):
    return n<0 and n%2!=0

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()
    return

#testy
head=Node(None)
a=Node(4)
head.next=a
b=Node(-7)
a.next=b
c=Node(15)
b.next=c
d=Node(12)
c.next=d
e=Node(-13)
d.next=e
f=Node(0)
e.next=f
wypisz(head.next)
A=Node(None)
B=Node(None)
C=rozdziel(head,A,B)
wypisz(A.next)
wypisz(B.next)
