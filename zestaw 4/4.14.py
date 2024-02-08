from random import randint

def countOnesInBinary(n):
    count=0
    while n>0:
        count+=n%2
        n//=2
    return count

def fun(T1,T2):
    n=len(T1)
    t1=[[countOnesInBinary(T1[i][j]) for i in range(n)] for j in range(n)]
    m=len(T2)
    t2=[None]*m
    for i in range(m):
        t2[i]=[None]*m
        for j in range(m):
            t2[i][j]=countOnesInBinary(T2[i][j])
    #n<m
    for i in range(m-n+1):
        for j in range(m-n+1):
            count=0
            for x in range(n):
                for y in range(n):
                    if t1[x][y]==t2[x+i][y+j]:
                        count+=1
            if 100*count>=33*n*n:
                return True
    return False
                        
N=int(input())
M=int(input())
while M<=N:
    M=int(input())
T1=[[randint(1,99) for _ in range(N)] for _ in range(N)]
T2=[[randint(1,99) for _ in range(M)] for _ in range(M)]
print(fun(T1,T2))
