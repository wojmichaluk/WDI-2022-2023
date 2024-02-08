from random import randint

def print_sums(T1,T2):
    n=len(T1)
    counter=0
    masks=3**n
    for mask in range(masks):
        decrypt=3**(n-1)
        suma=0
        for i in range(n):
            if mask-2*decrypt>=0:
                suma+=T2[n-1-i]
                mask-=2*decrypt
            elif mask-decrypt>=0:
                suma+=T1[n-1-i]
                mask-=decrypt
            else:
                suma+=T1[n-1-i]+T2[n-1-i]
            decrypt//=3
        if is_prime(suma):
            print(suma)
            counter+=1
    print("Znaleziono sum: ",end='')
    return counter

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

#sztywny przypadek dla N=5
#N=int(input())
N=5
T1=[randint(1,99) for _ in range(N)]
T2=[randint(1,99) for _ in range(N)]
print(print_sums(T1,T2))
