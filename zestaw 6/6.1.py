from math import log10

def primes(num,curr=0,i=1,flag=False):
    l=int(log10(num))+1
    if is_prime(curr) and curr>9 and flag and curr!=num:
        print(curr)
    if i==l+1:
        return False
    newnum=10*curr+(num//10**(l-i))%10
    return primes(num,newnum,i+1,True) or primes(num,curr,i+1)

def is_prime(n):
    if n<2:
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

n=int(input())
primes(n)
