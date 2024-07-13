from functools import cache

def fib(n):
    suma=0
    licznik=0
    def wew(n):
        nonlocal licznik
        licznik+=1
        nonlocal suma
        if n==1:
            suma+=1
            return 1
        a=wew(n-1)
        suma+=a
        return suma-a
    b=wew(n)
    print(licznik,end=' ')
    return b

@cache
def fib_rek(n):
    licznik=0
    def wew(n):
        nonlocal licznik
        licznik+=1
        if n==1 or n==2:
            return 1
        return wew(n-1)+wew(n-2)
    b=wew(n)
    print(licznik,end=' ')
    return b

n=41    
for i in range(1,n):
    print(fib(i))
    print(fib_rek(i))
    print()
