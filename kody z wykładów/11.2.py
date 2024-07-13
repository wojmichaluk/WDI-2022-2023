from random import randint
import time

def find(tab,el):
    p=0
    k=len(tab)-1
    while p<=k:
        sr=(p+k)//2
        if el==tab[sr]:
            return sr
        elif el>tab[sr]:
            p=sr+1
        else:
            k=sr-1
    return -1

def find_prop(tab,el):
    p=0
    k=len(tab)-1
    while p<=k:
        xa,xb=tab[p],tab[k]
        t=(el-xa)/(xb-xa)
        sr=int(p+t*(k-p))
        if el==tab[sr]:
            return sr
        elif el>tab[sr]:
            p=sr+1
        else:
            k=sr-1
    return -1

n=10000000
T=[randint(1,10000000) for _ in range(n)]
T.sort() #pomocniczo
el=T[12345]
print("start")
t1=time.time()
i=find(T,el)
t2=time.time()
print(i,T[i],t2-t1)
t1=time.time()
j=find_prop(T,el)
t2=time.time()
print(j,T[j],t2-t1)
