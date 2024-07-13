from random import randint

def ex_zero(T):
    n=len(T)
    z_w=[False for _ in range(n)]
    z_k=[False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if T[i][j]==0:
                z_w[i]=True
                z_k[j]=True
    for k in range(n):
        if not z_w[k] or not z_k[k]:
            return False
    return True

N=int(input())
T=[[randint(-1,1) for _ in range(N)] for _ in range(N)]
print(ex_zero(T))
