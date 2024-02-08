from random import randint

def same_digits(a,b):
    aa,bb=a,b
    T=[False for i in range(10)]
    while a>0:
        T[a%10]=True
        a//=10
    while b>0:
        if not T[b%10]:
            return False
        b//=10
    T=[False for i in range(10)]
    while bb>0:
        T[bb%10]=True
        bb//=10
    while aa>0:
        if not T[aa%10]:
            return False
        aa//=10
    return True

def friends(T):
    n=len(T)
    cnt=0
    for i in range(n):
        for j in range(n):
            flag=True
            for x,y in [(i,j-1), (i,j+1), (i-1,j), (i+1,j), (i-1,j-1), (i-1,j+1), (i+1,j-1), (i+1,j+1)]:
                if x<0 or x>=n or y<0 or y>=n:
                    continue
                if not same_digits(T[i][j], T[x][y]):
                    flag=False
                    break
            if flag:
                cnt+=1
    return cnt
            
N=int(input())
T=[[randint(1,99) for _ in range(N)] for _ in range(N)]
print(friends(T))
