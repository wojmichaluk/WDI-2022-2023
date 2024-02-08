from random import randint

def ones_in_bin(n):
    ones=0
    while n>0:
        ones+=n%2
        n//=2
    return ones

def trzy_pod(T,i=0,s1=0,s2=0,s3=0):
    if i==len(T):
        if s1>0 and s1==s2==s3:
            return True
        return False
    tmp=ones_in_bin(T[i])
    return trzy_pod(T,i+1,s1+tmp,s2,s3) or trzy_pod(T,i+1,s1,s2+tmp,s3) or trzy_pod(T,i+1,s1,s2,s3+tmp)

n=int(input())
T=[randint(1,99) for _ in range(n)]
print(trzy_pod(T))
