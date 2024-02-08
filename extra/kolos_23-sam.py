class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def wypisz(p):
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()

def zew(p):
    def usun(p):
        if p==None:
            return
        current=1
        longest=0
        longest_cnt=1
        r=p
        s=p.next
        while s!=None:
            if s.val==r.val:
                current+=1
            else:
                if current>longest:
                    longest=current
                    longest_cnt=1
                elif current==longest:
                    longest_cnt+=1
                current=1
            r=s
            s=s.next
        if current>longest:
            longest=current
            longest_cnt=1
        elif current==longest:
            longest_cnt+=1
        return longest,longest_cnt
    a=usun(p)
    if not a:
        return 0
    if a[1]>1:
        return 0
    #nie można usunąć pierwszego 
    r=p
    while r!=None:
        t=r
        flag=True
        for i in range(a[0]-1):
            if t.next.val!=t.val:
                flag=False
                break
            t=t.next
        if flag:
            s.next=t.next
            return a[0]
        s=r
        r=r.next

#testy
a=Node(1)
b=Node(3)
a.next=b
c=Node(3)
b.next=c
d=Node(5)
c.next=d
e=Node(3)
d.next=e
f=Node(3)
e.next=f
g=Node(3)
f.next=g
h=Node(3)
g.next=h
wypisz(a)
print(zew(a))
wypisz(a)
