from math import *

x=int(input())
i=floor(log10(x))+1
a=0
while x>0 and a!=i:
    a=x%10
    x//=10
print(a==i)
