from random import randint

suma=0

def detA(T,ilo=1):
    global suma
    n=len(T)
    if n==1:
        suma+= ilo*T[0][0]
    else:
        for i in range(n):
            new_T=new_tab(T,i,0)
            dop=(-1)**i*T[i][0]
            detA(new_T,ilo*dop)

def new_tab(T,i,j):
    m=len(T)
    T=T[:i]+T[i+1:]
    for k in range(m-1):
        T[k]=T[k][:j]+T[k][j+1:]
    return T

N=int(input())
T=[[randint(-9,9) for _ in range(N)] for _ in range(N)]
print(*T,sep='\n')
detA(T)
print(suma)
