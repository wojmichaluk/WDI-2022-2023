from math import *

def sum_p(n):
    x=n
    i=floor(log10(n))+1
    suma=0
    while x>0:
       suma+=(x%10)**i
       if suma>n:
           return False
       x//=10
    return suma==n

for i in range(1,1000000001):
    if sum_p(i):
        print(i)
print("Sprawdzono do 10^9.")
