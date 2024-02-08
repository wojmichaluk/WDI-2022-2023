from math import log10

primes=0

def build_from_two(num1,num2,l1,l2,curr=0):
    if l1==l2==0:
        if is_prime(curr):
            global primes
            primes+=1
    else:
        curr1=curr2=curr
        if l1>0:
            curr1=10*curr1+num1//10**(l1-1)
            n1=num1%(10**(l1-1))
            build_from_two(n1,num2,l1-1,l2,curr1)
        if l2>0:
            curr2=10*curr2+num2//10**(l2-1)
            n2=num2%(10**(l2-1))
            build_from_two(num1,n2,l1,l2-1,curr2)

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

num1=int(input())
num2=int(input())
len1=int(log10(num1))+1
len2=int(log10(num2))+1
build_from_two(num1,num2,len1,len2)
print(primes)
