from random import randint

def ile_parzystych_w_piatkowym(n):
    podstawa=5
    cnt=0
    m=n
    while m>0:
        cyfra=m%podstawa
        if cyfra%2==0:
            cnt+=1
        m//=podstawa
    return cnt

def zgodne_piatkowo(tab1,tab2):
    n=len(tab1)
    for i in range(n):
        for j in range(n):
            tab1[i][j]=ile_parzystych_w_piatkowym(tab1[i][j])
    N=len(tab2)
    M=N+2*n-2
    T=[[-1 for _ in range(M)] for _ in range(M)]
    for i in range(N):
        for j in range(N):
            T[i+n-1][j+n-1]=ile_parzystych_w_piatkowym(tab2[i][j])
    for i in range(M-n):
        for j in range(M-n):
            obszar=zgodne=0
            for k in range(i,i+n):
                for l in range(j,j+n):
                    if T[k][l]>=0:
                        obszar+=1
                        if T[k][l]==tab1[k-i][l-j]:
                            zgodne+=1
            if zgodne/obszar>=0.33:
                return True
    return False
                
MAX1=int(input())
MAX2=int(input())
while MAX2<=MAX1:
    MAX2=int(input())
tab1=[[randint(1,99) for _ in range(MAX1)] for _ in range(MAX1)]
tab2=[[randint(1,99) for _ in range(MAX2)] for _ in range(MAX2)]
print(zgodne_piatkowo(tab1,tab2))
