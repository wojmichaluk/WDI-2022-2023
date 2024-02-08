from random import randint

def singletons(T1,T2):
    n=len(T1)
    l=m=0
    while l!=n**2:
        smallest=0
        k=0
        while smallest==0 and k<N:
            smallest=T1[k][0]
            k+=1
        s_ind=k-1
        for j in range(0,N):
            if T1[j][0]!=0 and T1[j][0]<smallest:
                smallest=T1[j][0]
                s_ind=j
        T2[m]=T1[s_ind][0]
        for j in range(0,N):
            if T1[j][0]==smallest:
                T1[j]=T1[j][1:]+[0]
                l+=1
        m+=1
    return T2

N=int(input())
T1=[[0 for _ in range(N)] for _ in range(N)]
#zakładamy, że N<=100
for i in range(N):
    for j in range(N):
        temp=randint(1,100)
        while temp in T1[i]:
            temp=randint(1,100)
        T1[i][j]=temp
T2=[0 for _ in range(N*N)]
for i in range(N):
    T1[i].sort()
print(singletons(T1,T2))
