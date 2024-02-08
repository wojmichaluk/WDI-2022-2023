from random import randint

def only_even(T):
    for i in range(N):
        if even_row(T[i]):
            return True
    return False

def even_row(T):
    for element in T:
        if not(even_digit(element)):
            return False
    return True

def even_digit(n):
    while n>0:
        if (n%10)%2==0:
            return True
        n//=10
    return False

N=int(input())
T=[[randint(1,99) for _ in range(N)] for _ in range(N)]
print(only_even(T))
