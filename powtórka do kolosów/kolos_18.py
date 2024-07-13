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
    wartA=Node()
    wartB=Node()
    wartA.next=A
    wartB.next=B
    cnt=0
    prevB=wartB
    currB=B
    while currB!=None:
        prevA=wartA
        currA=A
        while currA!=None and currA.val<currB.val:
            prevA=prevA.next
            currA=currA.next
        if currA!=None and currA.val==currB.val:
            prevA.next=currA.next
            prevB.next=currB.next
            currA=currA.next
            currB=currB.next
            cnt+=1
        else:
            prevB=prevB.next
            currB=currB.next
    return cnt

#testy
a=Node(5)
b=Node(7)
a.next=b
c=Node(17)
b.next=c
d=Node(7)
e=Node(13)
d.next=e
f=Node(11)
e.next=f
g=Node(5)
f.next=g
wypisz(a)
wypisz(d)
print(fun(a,d))
#nie ma wartowników, więc pierwsze elementy się nie usuwają
#wersja z wartownikami - zadanie 28
wypisz(a)
wypisz(d)
