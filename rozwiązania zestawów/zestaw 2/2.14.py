from math import *

def mix_numbers(a,b,mask):
    num=0
    mult=1
    while mask>0 or a>0:
        if mask%2==0:
            d=a%10
            a//=10
        else:
            d=b%10
            b//=10
        mask//=2
        num=d*mult+num
        mult*=10
    return num

def validate_mask(a,b,mask):
    cnt1=get_leng(a)
    cnt2=get_leng(b)
    while mask>0:
        if mask%2==0:
            cnt1-=1
        else:
            cnt2-=1
        mask//=2
    return cnt1>=0 and cnt2==0

def is_prime(n):
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
        return True

def get_leng(n):
    return floor(log10(n))+1

cnt=0
a=int(input())
b=int(input())
for mask in range(2**(get_leng(a)+get_leng(b))):
    if validate_mask(a,b,mask) and is_prime(mix_numbers(a,b,mask)):
        cnt+=1
print(cnt)
