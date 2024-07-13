class Node:
    def __init__(self):
        self.val=None
        self.next=None

class Array:
    def __init__(self):
        self.first=None

    #pomocnicza
    def wypisz(self):
        p=self.first
        while p!=None and p.val!=None:
            print(p.val)
            p=p.next
        return

#iteracyjnie
def merge_iter(first1,first2):
    t=Node()
    if first1.val<=first2.val:
        t.val=first1.val
        first1=first1.next
    else:
        t.val=first2.val
        first2=first2.next
    q=t
    while first1!=None or first2!=None:
        r=Node()
        if first1==None:
            r.val=first2.val
            first2=first2.next
        elif first2==None:
            r.val=first1.val
            first1=first1.next
        else:
            if first1.val<=first2.val:
                r.val=first1.val
                first1=first1.next
            else:
                r.val=first2.val
                first2=first2.next
        t.next=r
        t=t.next  
    return q

#rekurencyjnie
def merge_rek(first1,first2):
    t=Node()
    if first1.val<=first2.val:
        t.val=first1.val
        first1=first1.next
    else:
        t.val=first2.val
        first2=first2.next
    q=t
    p=Node()
    t.next=p
    def merge_r(first1,first2,t):
        if first1!=None or first2!=None:
            p=Node()
            t.next=p
            if first1==None:
                t.val=first2.val
                merge_r(first1,first2.next,t.next)
            elif first2==None:
                t.val=first1.val
                merge_r(first1.next,first2,t.next)
            else:
                if first1.val<=first2.val:
                    t.val=first1.val
                    merge_r(first1.next,first2,t.next)
                else:
                    t.val=first2.val
                    merge_r(first1,first2.next,t.next) 
        return
    merge_r(first1,first2,t.next)
    return q

#testy
tab1=Array()
p=Node()
p.val=21
tab1.first=p
for i in range(10):
    p=Node()
    p.val=19-2*i
    p.next=tab1.first
    tab1.first=p
#tab1.wypisz()        
tab2=Array()
p=Node()
p.val=52
tab2.first=p
for i in range(10):
    p=Node()
    p.val=47-5*i
    p.next=tab2.first
    tab2.first=p
#tab2.wypisz()
tab3=Array()
tab3.first=merge_iter(tab1.first,tab2.first)
tab4=Array()
tab4.first=merge_rek(tab1.first,tab2.first)
tab3.wypisz()
print()
tab4.wypisz()
