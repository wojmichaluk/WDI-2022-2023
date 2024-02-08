from random import randint

def condition(n1,n2,p):
    return n1*n2==p

def mult_pairs(T,p):
    n=len(T)
    cnt=0
    for x in range(n):
        for y in range(n):
            for x2,y2 in [(x+1,y+2), (x+1,y-2), (x-1,y+2), (x-1,y-2), (x+2,y+1), (x+2,y-1), (x-2,y+1), (x-2,y-1)]:
                if x2<0 or x2>=n or y2<0 or y2>=n:
                    continue                    
                if condition(T[y][x], T[y2][x2], p):
                    cnt+=1
    return cnt//2

p=int(input())
N=int(input())
T=[[randint(1,9) for _ in range(N)] for _ in range(N)]
print(mult_pairs(T,p))
