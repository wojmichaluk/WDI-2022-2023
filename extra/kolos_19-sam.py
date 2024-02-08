from random import randint

#pomocnicza
def czynnikowo_podobne(m,n):
    p=m
    d=2
    wspolne=0
    while p>1:
        if p%d==0:
            if n%d==0:
                wspolne+=1
            while p%d==0:
                p//=d
        d+=1
        if wspolne>1:
            break
    return wspolne==1

#pomocnicza
def contains(w,k,n):
    return 0<=w<n and 0<=k<n

def three(T):
    n=len(T)
    num=0
    for w in range(n):
        for k in range(n):
            cp=0
            for x,y in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                if contains(w+x,k+y,n) and czynnikowo_podobne(T[w][k],T[w+x][k+y]):
                    cp+=1
            if cp==3:
                num+=1
    return num

#testy
#n=3
n=int(input())
T=[[randint(10,99) for _ in range(n)] for _ in range(n)]
#print(*T,sep='\n')
print(three(T))
