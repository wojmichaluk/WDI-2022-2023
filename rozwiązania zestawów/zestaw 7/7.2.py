class Node:
    def __init__(self):
        self.val=None
        self.next=None

class Array:
    def __init__(self):
        self.first=None
    def index_el(self,n):
        p=self.first
        i=0
        while p!=None:
            if i==n:
                return p.val
            p=p.next
            i+=1
        return None
    def sub(self,n,value):
        p=self.first
        i=0
        while p!=None:
            if i==n:
                p.val=value
                return
            p=p.next
            i+=1
        return None

    #pomocnicza
    def wypisz(self):
        p=self.first
        while p!=None:
            print(p.val)
            p=p.next
        return

#testy
tab=Array()
p=Node()
p.val=11
tab.first=p
for i in range(10):
    p=Node()
    p.val=10-i
    p.next=tab.first
    tab.first=p
tab.wypisz()        
print(tab.index_el(3))
print(tab.index_el(0))
print(tab.index_el(12))
print(tab.index_el(7))
tab.sub(4,99)
tab.sub(2,98)
tab.sub(9,97)
tab.sub(14,96)
tab.wypisz()
