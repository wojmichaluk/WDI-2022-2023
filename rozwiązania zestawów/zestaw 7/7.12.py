class Node:
    def __init__(self,value):
        self.val=value
        self.next=None

#jeżeli wywołane tylko raz - nie trzeba globala
def insert(el,zb1):
    global zb
    r=zb1
    q=None
    while r!=None and r.val<el:
        q=r
        r=r.next
    if r!=None and r.val==el:
        return False
    p=Node(el)
    p.next=r
    if q!=None:
        q.next=p
    else:
        zb=p
    return True

#pomocnicza
def wypisz(zb):
    p=zb
    while p!=None:
        print(p.val,end=' ')
        p=p.next
    print()
    return

#testy
zb=Node("pies")
wypisz(zb)
print(insert("kot",zb))
wypisz(zb)
print(insert("kocur",zb))
print(insert("szczeniak",zb))
print(insert("pies",zb))
print(insert("bażant",zb))
print(insert("zebra",zb))
print(insert("kocur",zb))
wypisz(zb)
