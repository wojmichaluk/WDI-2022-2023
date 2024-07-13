def bin_prime(A,B,x):
    if A==0 and B==0:
        if is_composite(x):
            return 1
        return 0
    a=0
    b=0
    if A>0:
        a=bin_prime(A-1,B,x+2**(A+B-1))
    if B>0:
        b=bin_prime(A,B-1,x)
    return a+b

def is_composite(n):
    if n<4:
        return False
    elif n%2==0:
        return True
    else:
        i=3
        while i*i<=n:
            if n%i==0:
                return True
            i+=2
        return False

A=int(input())
B=int(input())
x=2**(A+B-1)
print(bin_prime(A-1,B,x))
