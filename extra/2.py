from random import randint
from math import gcd

def sum_p(n):
    i=0
    y=x=n
    while n>0:
        n//=10
        i+=1
    suma=0
    while x>0:
       suma+=(x%10)**i
       x//=10
       if suma>y:
           return False
    return suma==y

#podejście naiwne
"""def prime(n):
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
        return True"""

#podejście probabilistyczne
def prime(p,n=100):
    if p<2:
        return False
    if p==2 or p==3:
        return True
    if p%2==0:
        return False
    for i in range(n):
        a=randint(2,p-1)
        if gcd(a,p)!=1:
            return False
        if pow(a,p-1,p)!=1:
            return False
    return True
    
i=1
while i<10**60:
    if sum_p(i):
        if prime(i):
            print(i)
    i+=1
