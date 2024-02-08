class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def wypisz(p):
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()

#zakładam, że iloraz jest całkowity
def zbadaj_iloraz(p):
    def repair(p):
        nonlocal d
        nonlocal first
        r=p
        while r!=None:
            r.val*=first
            r=r.next
        wypisz(p)
        r=p
        iloraz=d
        suma=0
        while r.next!=None:
            if r.val*iloraz!=r.next.val:
                t=Node(r.val*iloraz)
                s=t
                suma+=1
                while iloraz*t.val!=r.next.val:
                    suma+=1
                    t.next=Node(iloraz*t.val)
                    t=t.next
                t.next=r.next
                r.next=s
                r=t.next
            else:
                r=r.next
        return suma
    r=p
    first=r.val
    while r!=None:
        r.val//=first
        r=r.next
    d=2
    while d<=abs(p.next.val):
        flag=1
        r=p
        while r!=None:
            s=r.val
            while s%d==0:
                s//=d
            if s!=1:
                flag=0
                break
            r=r.next
        if flag==1:
            return repair(p)
        flag=1
        r=p
        d*=-1
        while r!=None:
            s=r.val
            while s%d==0:
                s//=d
            if s!=1:
                flag=0
                break
            r=r.next
        if flag==1:
            return repair(p)
        d*=-1
        d+=1
    
a=Node(4)
b=Node(-32)
a.next=b
c=Node(-128)
b.next=c
d=Node(-2048)
c.next=d
wypisz(a)
print(zbadaj_iloraz(a))
wypisz(a)
