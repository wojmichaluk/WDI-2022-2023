def smith(n):
    x=n
    suma=0
    while n%2==0:
        suma+=2
        n//=2
    i=3
    while i*i<=n:
        if n%i==0 and prime(i):
            while n%i==0:
                suma+=suma_cyfr(i)
                n//=i
            i=3
        i+=2
    if n==1:
        return suma==suma_cyfr(x)
    else:
        return suma+suma_cyfr(n)==suma_cyfr(x)

def prime(n):
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
    
def suma_cyfr(n):
    suma=0
    while n>0:
        suma+=n%10
        n//=10
    return suma

for i in range(1,1000000):
    if not(prime(i)) and smith(i):
        print(i)

