from random import randint

def fun(T):
    n=len(T)
    for i in range(n):
        if not rows(T[i]):
            return False
    return True

def rows(tab):
    m=len(tab)
    for i in range(m):
        if only_prime_digits(tab[i]):
            return True
    return False

def only_prime_digits(n):
    tmp=n
    while tmp>0:
        if tmp%10 not in [2,3,5,7]:
            return False
        tmp//=10
    return True

N=int(input())
T=[[randint(100,999) for _ in range(N)] for _ in range(N)]
print(fun(T))
