from random import randint

def max_sum(T):
    n=len(T)
    max_suma=T[0][0]
    for w in range(n):
        for k in range(n):
            for i in range(1,11):
                suma=0
                for x in range(w,min(i+w,n)):
                    suma+=T[x][k]
                max_suma=max(max_suma,suma)
                suma=0
                for x in range(k,min(i+k,n)):
                    suma+=T[w][x]
                max_suma=max(max_suma,suma)
    return max_suma

N=int(input())
T=[[randint(-99,99) for _ in range(N)] for _ in range(N)]
print(max_sum(T))
