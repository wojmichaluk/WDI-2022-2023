from random import randint

def jumps(T,i=0,skoki=0):
    if i>=len(T):
        return -1
    if i==len(T)-1:
        return skoki
    J=primes(T[i])
    for s in J:
        sk=jumps(T,i+s,skoki+1)
        if sk>0:
            return sk
    return -1

def primes(n):
    P=[0 for _ in range(n)]
    i=0
    div=2
    kopia_n=n
    while div<n//2+1:
        if kopia_n%div==0:
            P[i]=div
            i+=1
            while kopia_n%div==0:
                kopia_n//=div
        div+=1
    return P[:i]

n=int(input())
T=[randint(1,30) for _ in range(n)]
print(jumps(T))
