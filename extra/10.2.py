from random import randint
from math import log2

cnt=1

def qs(T,l,p,k):
    i=l
    j=p
    x=T[(l+p)//2]
    while i<=j:
        while T[i]<x:
            i+=1
        while T[j]>x:
            j-=1
        if i<=j:
            T[j],T[i]=T[i],T[j]
            i+=1
            j-=1
    if l<j:
        qs(T,l,j,k)
    if i<p:
        qs(T,i,p,k)
    #prymitywne rozwiązanie
    global cnt
    if not(l<j or i<p):
        if cnt==int(log2(k))+1:
            suma=0
            for m in range(k):
                suma+=T[m]
            print(suma)
        cnt+=1
        return
    
n=1000000
k=50
T=[randint(1,1000000) for _ in range(n)]
qs(T,0,n-1,k)
for i in range(min(2*k-1,n)):
    print(T[i],end=' ')
print()
