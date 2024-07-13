from random import randint

def podzbiory(T,k,i=0,suma1=0,suma2=0):
    if k>len(T):
        return False
    if k==0:
        return suma1==suma2
    if i==len(T):
        return False
    return podzbiory(T,k,i+1,suma1,suma2) or podzbiory(T,k-1,i+1,suma1+T[i],suma2) or podzbiory(T,k-1,i+1,suma1,suma2+T[i])

n=int(input())
k=int(input())
T=[randint(1,99) for _ in range(n)]
print(podzbiory(T,k))
