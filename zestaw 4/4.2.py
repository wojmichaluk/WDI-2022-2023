from random import randint

def only_odd(T):
    for i in range(N):
        if not(odd_row(T[i])):
            return False
    return True

def odd_row(T):
    for element in T:
        if odd_digits(element):
            return True
    return False

def odd_digits(n):
    while n>0:
        if (n%10)%2==0:
            return False
        n//=10
    return True

N=int(input())
T=[[randint(1,99) for _ in range(N)] for _ in range(N)]
print(only_odd(T))
