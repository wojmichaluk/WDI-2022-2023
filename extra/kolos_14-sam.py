from random import randint

def wiel_kwad(n):
    if n<8:
        return 0
    i=2
    while i*i<=n//2:
        if n%(i*i)==0:
            return 1
        i+=1
    return 0

def suma_tab_jednowym(T):
    suma=0
    for elem in T:
        suma+=elem
    return suma

def czy_mozna_usunac(T):
    n=len(T)
    suma=0
    for i in range(n):
        for j in range(n):
            T[i][j]=wiel_kwad(T[i][j])
            suma+=T[i][j]
    if suma<n*n-3*n+2:
        return False
    for i in range(n):
        for j in range(n-1):
            for k in range(j+1,n):
                w1=suma_tab_jednowym(T[i])
                tab1=[T[i][j] for _ in range(n)]
                tab2=[T[i][k] for _ in range(n)]
                k1=suma_tab_jednowym(tab1)
                k2=suma_tab_jednowym(tab2)
                if suma-w1-k1-k2==n*n-3*n+2:
                    return True
    return False

T=[[randint(5,99) for _ in range(5)] for _ in range(5)]
print(*T,sep='\n')
print(czy_mozna_usunac(T))
print(*T,sep='\n')
