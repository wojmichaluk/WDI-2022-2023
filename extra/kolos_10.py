from math import log10

def divide(n,parts=0):
    if n==0:
        return is_prime(parts)
    length=int(log10(n))+1
    for cut_len in range(1,length+1):
        prefix=n//(10**(length-cut_len))
        new_n=n%(10**(length-cut_len))
        if is_prime(prefix) and divide(new_n,parts+1):
            return True
    return False

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
print(divide(n))
