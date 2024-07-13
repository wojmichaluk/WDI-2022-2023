from random import randint
from math import gcd

#metoda naiwna
"""def czy_pierwsza(x):
    n=int(x**0.5)
    if x%2==0:
        return False
    i=3
    while i<=n:
        if x%i==0:
            return False
        i+=2
    return True"""

#metoda probabilistyczna
def czy_pierwsza(p,n=100):
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

def suma_cyfr(x):
    suma=0
    while x>0:
        suma+=x%10
        x//=10
    return suma

i=99999999999
while True:
    if suma_cyfr(i)==101:
        if czy_pierwsza(i):
            print(i)
            break
    i+=1
