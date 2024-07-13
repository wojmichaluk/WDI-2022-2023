from random import randint

def biggest_sum(T):
    n=len(T)
    maks=0
    mw=mk=0
    for x in range(n):
        for y in range(n):
            suma=0
            for i,j in [(x-1,y+1), (x,y+1), (x+1,y+1), (x-1,y), (x+1,y), (x-1,y-1), (x,y-1), (x+1,y-1)]:
                if i<0 or i>=n or j<0 or j>=n:
                    continue
                suma+=T[i][j]
            if suma>maks:
                maks=suma
                mw=x
                mk=y
    return mw,mk

N=int(input())
T=[[randint(1,9) for _ in range(N)] for _  in range(N)]
print(biggest_sum(T))
