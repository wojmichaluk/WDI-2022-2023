from random import randint

def suma_w_tab(T,suma):
    if len(T)==1:
        if T[0][0]==suma:
            return True
        return False
    elif suma>0:
        n=len(T)
        for i in range(n):
            for j in range(n):
                new_t=new_tab(T,i,j)
                if suma_w_tab(new_t,suma-T[i][j]):
                    return True
    return False

def new_tab(T,i,j):
    n=len(T)
    T=T[:i]+T[i+1:]
    for k in range(n-1):
        T[k]=T[k][:j]+T[k][j+1:]
    return T

n=8
#n=int(input())
suma=int(input())
T=[[randint(1,9) for _ in range(n)] for _ in range(n)]
print(suma_w_tab(T,suma))
#print(*T,sep='\n')
