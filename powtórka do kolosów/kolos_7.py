from random import randint
from math import inf

def minimum(T,r,c):
    if r==0 and c==0:
        return 0
    if r<0 or c<0:
        return inf
    return min(minimum(T,r-1,c),minimum(T,r,c-1))+T[r][c]

n=int(input())
T=[[randint(1,9) for _ in range(n)] for _ in range(n)]
T[0][0]=T[n-1][n-1]=0
print(minimum(T,n-1,n-1))
print(*T,sep='\n')
