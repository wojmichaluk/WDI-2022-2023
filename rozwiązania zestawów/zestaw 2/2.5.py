from math import *

def number(n,mask):
    num=0
    mult=1
    while mask>0:
        if mask%2==1:
            d=n%10
            num=d*mult+num
            mult*=10
        n//=10
        mask//=2
    return num

n=int(input())
l=floor(log10(n))+1
count=0
for i in range(1,2**l):
    t=number(n,i)
    if t%7==0:
        count+=1
print(count)
