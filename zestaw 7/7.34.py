class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

#pomocnicze
class Node2:
    def __init__(self,key,cnt):
        self.key=key
        self.cnt=cnt
        self.next=None

def delete(ptr,el):
    a=ptr
    q=ptr
    b=ptr.next
    flag=True
    while b!=a:
        if b.val==el:
            q.next=b.next
            if flag:
                a.next=b.next
        else:
            q=b
            flag=False
        b=b.next
    return a

def add_to_tmp(ptr,key):
    p=ptr
    r=ptr.next
    while r!=None and r.key<key:
        p=r
        r=r.next
    t=Node2(key,1)
    p.next=t
    t.next=r
    return

def increase(ptr,key):
    p=ptr
    while p.key!=key:
        p=p.next
    p.cnt+=1
    return

def member(ptr,key):
    p=ptr
    while p!=None and p.key!=key:
        p=p.next
    return p!=None

def wypisz(node):
    if node!=None:
        a=node
        b=node.next
        print(a.val,end=' ')
        while b!=a:
            print(b.val,end=' ')
            b=b.next
        print()

def wypisz2(t):
    while t!=None:
        print(t.key,t.cnt,end='   ')
        t=t.next
    print()
    return

def a_cnt(ptr,key):
    p=ptr
    while p.key!=key:
        p=p.next
    return p.cnt

#właściwa
def usun_z_cyklu(ptr,k):
    a=ptr
    b=ptr
    t=Node2(None,None)
    flag=True
    while b!=a or flag:
        if member(t.next,b.val):
            increase(t.next,b.val)
        else:
            add_to_tmp(t,b.val)
        b=b.next
        flag=False
        wypisz2(t.next)
    s=t.next
    t=t.next
    flag2=False
    while t!=None:
        if t.cnt==k:
            a=delete(a,t.key)
            flag2=True
        t=t.next
    """num=a_cnt(s,a.val)
    if num==k:
        if a==a.next:
            a=None
        else:
            b=a
            while b.next!=a:
                b=b.next
            b.next=a.next
            a=None"""
    return flag2
    
#testy
a=Node(7)
b=Node(5)
a.next=b
c=Node(13)
b.next=c
d=Node(15)
c.next=d
e=Node(7)
d.next=e
f=Node(15)
e.next=f
g=Node(25)
f.next=g
h=Node(13)
g.next=h
i=Node(7)
h.next=i
i.next=a
wypisz(a)
#niestety, nie usuwa pierwszego elementu...
print(usun_z_cyklu(a,2))
wypisz(a)
