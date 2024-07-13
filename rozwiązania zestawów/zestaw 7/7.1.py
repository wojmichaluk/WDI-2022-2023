class Node:
    def __init__(self):
        self.val=None
        self.next=None

class Zbior_n:
    def __init__(self):
        self.first=None
    def belongs(self,value):
        p=self.first
        while p!=None:
            if p.val==value:
                return True
            p=p.next
        return False
    def insert(self,p,value):
        if p==self.first:
            n=Node()
            n.val=value
            n.next=self.first
            self.first=n
            return
        q=None
        n=Node()
        r=self.first
        while r!=p:
            q=r
            r=r.next
        n.val=value
        q.next=n
        n.next=p
        return
    def delete(self,value):
        r=self.first
        if r.val==value:
            self.first=r.next
            return
        q=None
        while r.val!=value:
            q=r
            r=r.next
        q.next=r.next

    #pomocnicza
    def wypisz(self):
        p=self.first
        while p!=None:
            print(p.val)
            p=p.next
        return

#testy
N=Zbior_n()
p=Node()
p.val=11
N.first=p
for i in range(10):
    N.insert(p,i+1)
N.wypisz()        
print(N.belongs(3))
print(N.belongs(7))
print(N.belongs(13))
print(N.belongs(31))
N.delete(1)
N.delete(7)
N.wypisz()
