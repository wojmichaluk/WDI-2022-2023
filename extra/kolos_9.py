from random import randint

def skoczek(T):
    n=len(T)
    def rek(w,k,i=0):
        if k<0 or k>=n or w>=n:
            return float("inf")
        if T[w][k]==True:
            return float("inf")
        if w==n-1:
            return i
        return min(rek(w+1,k-2,i+1),rek(w+2,k-1,i+1),rek(w+2,k+1,i+1),rek(w+1,k+2,i+1))
    ans=float("inf")
    for k in range(n):
        ans=min(ans,rek(0,k))
    return ans    

n=int(input())
T=[[(1+(-1)**randint(1,2))//2 for _ in range(n)] for _ in range(n)]
print(skoczek(T))
print(*T,sep='\n')
