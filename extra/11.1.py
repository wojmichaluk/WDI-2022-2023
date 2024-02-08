from random import randint
import time

#rekurencyjnie
def find2(tab,el,p,k):
    if p>k:
        return -1
    sr=(p+k)//2
    if tab[sr]==el:
        return sr
    if el>tab[sr]:
        return find2(tab,el,sr+1,k)
    return find2(tab,el,p,sr-1)

def find3(tab,el,p,k):
    if p>k:
        return -1
    sr1=p+(k-p)//3
    sr2=p+(2*(k-p))//3
    if tab[sr1]==el:
        return sr1
    if tab[sr2]==el:
        return sr2
    if el<tab[sr1]:
        return find3(tab,el,p,sr1-1)
    if el>tab[sr2]:
        return find3(tab,el,sr2+1,k)
    return find3(tab,el,sr1+1,sr2-1)

"""#iteracyjnie
def find2(tab,el):
    p=0
    k=len(tab)-1
    while p<=k:
        sr=(p+k)//2
        print(sr)
        if el==tab[sr]:
            return sr
        elif el>tab[sr]:
            p=sr+1
        else:
            k=sr-1
    return -1

def find3(tab,el):
    p=0
    k=len(tab)-1
    while p<=k:
        sr1=p+(k-p)//3
        sr2=p+(2*(k-p))//3
        print(sr1,sr2)
        if el==tab[sr1]:
            return sr1
        elif el==tab[sr2]:
            return sr2
        elif el>tab[sr2]:
            p=sr2+1
        elif el<tab[sr1]:
            k=sr1-1
        else:
            p=sr1+1
            k=sr2-1
    return -1"""

n=100000000
T=[randint(1,10000000) for _ in range(n)]
T.sort() #pomocniczo
el=T[12345]
print("start")
t1=time.time()
i=find2(T,el,0,len(T)-1)
t2=time.time()
print(i,T[i],t2-t1)
t1=time.time()
j=find3(T,el,0,len(T)-1)
t2=time.time()
print(j,T[j],t2-t1)
