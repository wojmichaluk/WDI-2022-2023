import time

class Node:
    def __init__(self):
        self.val=None
        self.next=None

#pomocnicza
def wypisz(first):
    p=first
    while p!=None:
        print(p.val)
        p=p.next
    return
    
#iteracyjnie
def merge(p1,p2):
    if p1==None:
        return p2
    if p2==None:
        return p1
    if p1.val>p2.val:
        head=p2
        p2=p2.next
    else:
        head=p1
        p1=p1.next
    last=head
    while p1!=None and p2!=None:
        if p1.val>p2.val:
            last.next=p2
            p2=p2.next
        else:
            last.next=p1
            p1=p1.next
        last=last.next
    if p1==None:
        last.next=p2
    else:
        last.next=p1
    return head

#rekurencyjnie
def merge_rek(p1,p2):
    if p1==None:
        return p2
    if p2==None:
        return p1
    if p1.val<p2.val:
        head=p1
        head.next=merge_rek(p1.next,p2)
    else:
        head=p2
        head.next=merge_rek(p1,p2.next)
    return head

#testy
p1=Node()
p1.val=1
p2=Node()
p2.val=1
h1,h2=p1,p2
for i in range(1,11):
    p=Node()
    p.val=1+2*i
    p1.next=p
    p1=p1.next
    r=Node()
    r.val=1+5*i
    p2.next=r
    p2=p2.next
wypisz(h1)        
print()
wypisz(h2)
#nie można oboma sposobami zadziałać na h1 i h2
#-nie wiem czemu
#h3=merge(h1,h2)
#print()
#wypisz(h3)
h4=merge_rek(h1,h2)
print()
wypisz(h4)
