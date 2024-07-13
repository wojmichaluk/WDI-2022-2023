from random import randint

def fun(T):
    n=len(T)
    for i in range(n):
        if rows(T[i]):
            return True
    return False

def rows(tab):
    m=len(tab)
    for i in range(m):
        if not contains_prime_digit(tab[i]):
            return False
    return True

def contains_prime_digit(n):
    tmp=n
    while tmp>0:
        if tmp%10 in [2,3,5,7]:
            return True
        tmp//=10
    return False

N=int(input())
T=[[randint(100,999) for _ in range(N)] for _ in range(N)]
print(fun(T))
