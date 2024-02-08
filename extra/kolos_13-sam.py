from random import randint

def krole(T,w=0,suma=0,last=-2):
    n=len(T)
    if w==n:
        return suma==0
    for k in range(n):
        if abs(k-last)>=2:
            if krole(T,w+1,suma+T[w][k],k):
                return True
    return False

T=[[randint(-9,9) for _ in range(8)] for _ in range(8)]
print(krole(T))
print(*T,sep='\n')
