from random import randint

def condition(x1,y1,x2,y2,m):
    return x1*y1*x2*y2==m

def check_mult(T,k):
    n=len(T)
    a=3
    while a<=n:
        for i in range(n-a+1):
            for j in range(n-a+1):
                if condition(T[i][j],T[i][j+a-1],T[i+a-1][j],T[i+a-1][j+a-1],k):
                    return True,(i+a//2,j+a//2)
        a+=2
    return False

k=int(input())
N=int(input())
T=[[randint(1,9) for _ in range(N)] for _ in range(N)]
print(check_mult(T,k))
