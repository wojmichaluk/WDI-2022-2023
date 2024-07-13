class Node:
    def __init__(self,power,wsp,next=None):
        self.power=power
        self.wsp=wsp
        self.next=next

#pomocnicza
def wypisz(zb):
    p=zb
    while p.next!=None:
        print(p.wsp,'*x^',p.power,'+',sep='',end='')
        p=p.next
    print(p.wsp,'*x^',p.power,sep='')
    return

def substract(a,b):
    if b==None:
        return a
    if a==None:
        c=Node(b.power,b.wsp*(-1))
        c.next=substract(a,b.next)
        return c
    if a.power==b.power:
        c=Node(a.power,a.wsp)
        c.wsp-=b.wsp
        c.next=substract(a.next,b.next)
        return c
    else:
        if a.power<b.power:
            c=Node(a.power,a.wsp)
            c.next=substract(a.next,b)
            return c
        else:
            c=Node(b.power,b.wsp*(-1))
            c.next=substract(a,b.next)
            return c

#testy
head1=Node(0,3)
a=Node(1,2)
head1.next=a
b=Node(2,1)
a.next=b
wypisz(head1)
head2=Node(0,2)
c=Node(2,4)
head2.next=c
d=Node(3,-1)
c.next=d
wypisz(head2)
e=substract(head1,head2)
wypisz(e)
#wypisz(head1)
#wypisz(head2)
