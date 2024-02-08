def knight(T,w,k,n):
    T[w][k]=n
    if n==len(T)**2:
        return True
    jumps=[(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
    for jump in jumps:
        next_w=w+jump[0]
        next_k=k+jump[1]
        if contains(T,next_w,next_k) and T[next_w][next_k]==0:
            if knight(T,next_w,next_k,n+1):
                return True
    T[w][k]=0
    return False

def contains(T,w,k):
    if 0<=w<len(T) and 0<=k<len(T):
        return True
    return False

N=int(input())
T=[[0 for _ in range(N)] for _ in range(N)]
print(knight(T,0,0,1))
for row in T:
    print(row)
