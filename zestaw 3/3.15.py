from random import randint

def fun(T):
    F=[0 for _ in range(N)]
    #zakładamy, że N jest duże
    F[0]=F[1]=1
    i=1
    while F[i]<N:
        F[i+1]=F[i]+F[i-1]
        i+=1
    for j in range(i):
        if not nprime(T[F[j]]):
            return False
    for k in range(N):
        if prime(T[k]):
            return True
    return False

def prime(n):
    if n==0 or n==1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        i=3
        while i*i<=n:
            if n%i==0:
                return False
            i+=2
        return True

def nprime(n):
    if n==0 or n==1:
        return False
    elif prime(n):
        return False
    else:
        return True

N=int(input())
T=[randint(0,10000) for _ in range(N)]
print(fun(T))

