def divide(N):
    Ns=str(N)
    n=len(Ns)
    for i in range(2**n):
        if i%2==0:
            continue
        binary=toBin(i,n)
        s=''
        podzialy=0
        flag=True
        for j in range(n):
            s+=Ns[j]
            if binary[j]=='1':
                podzialy+=1
                if not is_prime(int(s)):
                    flag=False
                s=''
        if flag and is_prime(podzialy):
            return True
    return False

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

def toBin(n,l):
    num=n
    s=l*'0'
    i=0
    while num>0:
        s=s[:i]+str(num%2)+s[i+1:]
        num//=2
        i+=1
    return s[-1::-1]

N=int(input())
print(divide(N))
