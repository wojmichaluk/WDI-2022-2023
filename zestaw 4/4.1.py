def spirala(T):
    n=len(T)
    l=1
    a,b=0,n-1
    while a<=b:
        for i in range(a,b+1):
            T[a][i]=l
            l+=1
        for j in range(a+1,b):
            T[j][b]=l
            l+=1
        for k in range(b,a,-1):
            T[b][k]=l
            l+=1
        for m in range(b,a,-1):
            T[m][a]=l
            l+=1
        a+=1
        b-=1
    return

N=int(input())
T=[[0 for _ in range(N)] for _ in range(N)]
spirala(T)
for i in range(N):
    print(T[i])
