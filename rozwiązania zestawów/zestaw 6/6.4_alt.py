def skoczek(T,w=0,k=0,n=1):
    T[w][k]=n
    if n==len(T)**2:
        wypisz(T)
        return
    for i in range(8):
        r=mozliwe(T,w,k,i)
        if r:
            skoczek(T,r[0],r[1],n+1)
    T[w][k]=0

def wypisz(T):
    print(*T,sep='\n')

def mozliwe(T,w,k,i):
    lines=(-2,-1,1,2,2,1,-1,-2)
    cols=(1,2,2,1,-1,-2,-2,-1)
    new_w=w+lines[i]
    new_k=k+cols[i]
    if 0<=new_w<8 and 0<=new_k<8 and T[new_w][new_k]==0:
        return new_w,new_k
    return False

#sztywny przypadek dla n=8
T=[[0 for _ in range(8)] for _ in range(8)]
skoczek(T)
