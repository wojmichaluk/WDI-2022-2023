from random import randint

def is_prime(n):
    if n==2:
        return True
    elif n%2==0:
        return False
    else:
        i=3
        while i*i<=n:
            if n%i==0:
                return False
            i+=2
        return True

def is_not_prime(n):
    if n==0 or n==1:
        return False
    else:
        return not is_prime(n)

def condition(T,x,y,z):
    cnt=0
    for i,j in [(x+1,y), (x-1,y), (x,y-1), (x,y+1), (x+1,y+1), (x+1,y-1), (x-1,y-1), (x-1,y+1)]:
        if T[i][j][z]:
            cnt+=1        
    return cnt

def find(T):
    n=len(T)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                T[i][j][k]=is_not_prime(T[i][j][k])
    level_count=-1
    for z in range(n):
        curr_count=0
        for x in range(1,n-1):
            for y in range(1,n-1):
                nbh=condition(T,x,y,z)
                if nbh>=6:
                    curr_count+=1
        if level_count==-1:
            level_count=curr_count
        else:
            if level_count!=curr_count:
                return False
    return True

N=int(input())
T=[[[randint(1,99) for _ in range(N)] for _ in range(N)] for _ in range(N)]
print(find(T))
