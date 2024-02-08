from random import randint

def check(T):
    n=len(T)
    T2=[False for _ in range(n)]
    T2[0]=True
    for i in range(n):
        if T2[i]:
            temp=T[i]
            k=2
            while temp!=1:
                while temp%k==0:
                    if i+k<n:
                        T2[i+k]=True
                    temp//=k
                k+=1
    return T2[n-1]

#sztywny przypadek dla N=20
#N=int(input())
N=20
T=[randint(1,1000) for _ in range(N)]
print(check(T))
