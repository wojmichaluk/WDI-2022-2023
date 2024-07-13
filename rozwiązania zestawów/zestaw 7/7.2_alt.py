class Node:
    def __init__(self,index,value):
        self.index=index
        self.val=value
        self.next=None

class Array:
    def __init__(self,lo=0,hi=1000,default=0):
        self.head=None
        self.low=lo
        self.high=hi
        self.default=default

def val(ar,ind):
    r=ar.head
    while r!=None and r.index<ind:
        r=r.next
    if r!=None and r.index==ind:
        return r.val
    else:
        if ar.low<=ind<=ar.high:
            return ar.default
        print("Nie udało się znaleźć-poza zakresem. Zwracam None")
        return None

def set_v(ar,ind,el):
    #pomocnicza
    def insert(el,ind,ar):
        if ar.head==None:
            if el!=ar.default:
                ar.head=Node(ind,el)
                return ar
            return None
        r=ar.head
        while r!=None:
            if r.index==ind:
                return ar
            r=r.next
        r=ar.head
        q=None
        while r!=None and r.index<ind:
            q=r
            r=r.next
        p=Node(ind,el)
        if r==None:
            q.next=p
            return ar
        p.next=r
        if q==None:
            ar.head=p
            return ar
        else:
            q.next=p
            return ar
    if ind<ar.low or ind>ar.high:
        print("Poza zakresem.")
        return ar
    r=ar.head
    q=None
    while r!=None and r.index<ind:
        q=r
        r=r.next
    if r!=None and r.index==ind:
        if el==ar.default:
            if q==None:
                ar.head=r.next
                return ar
            q.next=r.next
        else:
            r.val=el
        return ar
    else:
        return insert(el,ind,ar)

#pomocnicza
def wypisz(ar):
    p=ar.head
    while p!=None:
        print("Wartość:",p.val,"\tindeks:",p.index)
        p=p.next
    return

#testy
T=Array()
p=Node(10,5)
T.head=p
T=set_v(T,20,12)
T=set_v(T,1,100)
T=set_v(T,12,7)
T=set_v(T,100,3)
T=set_v(T,1001,6)
T=set_v(T,20,6)
T=set_v(T,100,6)
T=set_v(T,20,0)
wypisz(T)
print(val(T,35))
print(val(T,10))
print(val(T,-6))
