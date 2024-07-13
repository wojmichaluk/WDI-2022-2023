from random import randint

def sorting(T1,T2):
    for i in range(N*N):
        smallest=T1[0][0]
        k=1
        while smallest==0:
            smallest=T1[k][0]
            k+=1
        s_ind=0
        for j in range(1,N):
            if T1[j][0]!=0 and T1[j][0]<=smallest:
                smallest=T1[j][0]
                s_ind=j
        T2[i]=T1[s_ind][0]
        T1[s_ind]=T1[s_ind][1:]+[0]
    return T2       
    
N=int(input())
T1=[[randint(1,99) for _ in range(N)] for _ in range(N)]
T2=[0 for _ in range(N*N)]
for i in range(N):
    T1[i].sort()
print(sorting(T1,T2))
