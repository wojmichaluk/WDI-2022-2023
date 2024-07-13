from random import randint

def no_comp(T):
    n=len(T)
    for i in range(n):
        for j in range(n):
            #przyjmujemy, że dla 1 liczbą komplementarną może być ona sama
            if not is_comp(T[i][j], T):
                T[i][j]=0
    return

def is_comp(n, T):
    l=len(T)
    for i in range(l):
        for j in range(l):
            if T[i][j]!=0:
                if is_prime(n+T[i][j]):
                    return True
    return False

def is_prime(n):
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

N=int(input())
T=[[randint(1,99) for _ in range(N)] for _ in range(N)]
no_comp(T)
