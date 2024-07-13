from random import randint

"""def race(T):
    left_speed=left_rook(T,0,0)
    right_speed=right_rook(T,len(T)-1,0)
    if left_speed>right_speed:
        return 1
    elif left_speed<right_speed:
        return 2
    else:
        return 0

def left_rook(T,x,y):
    n=len(T)
    if x==y==n-1:
        return 0
    best_path=float("inf")
    for new_x in range(x+1,n):
        if nwd(T[y][x],T[y][new_x])==1:
            best_path=min(best_path,left_rook(T,new_x,y)+1)
    for new_y in range(y+1,n):
        if nwd(T[y][x],T[new_y][x])==1:
            best_path=min(best_path,left_rook(T,x,new_y)+1)
    return best_path

def right_rook(T,x,y):
    n=len(T)
    if x==0 and y==n-1:
        return 0
    best_path=float("inf")
    for new_x in range(x):
        if nwd(T[y][x],T[y][new_x])==1:
            best_path=min(best_path,left_rook(T,new_x,y)+1)
    for new_y in range(y+1,n):
        if nwd(T[y][x],T[new_y][x])==1:
            best_path=min(best_path,left_rook(T,x,new_y)+1)
    return best_path"""

def btr_race(T):
    n=len(T)
    left_speed=rook(T,0,0,(n-1,n-1),False)
    right_speed=rook(T,n-1,0,(0,n-1),True)
    print(left_speed,right_speed)
    if left_speed<right_speed:
        return 1
    elif left_speed>right_speed:
        return 2
    else:
        return 0

def rook(T,x,y,target,going_left):
    n=len(T)
    if (x,y)==target:
        return 0
    best_path=float("inf")
    if going_left:
        for new_x in range(x):
            if nwd(T[y][x],T[y][new_x])==1:
                best_path=min(best_path,rook(T,new_x,y,target,going_left)+1)
    else:
        for new_x in range(x+1,n):
            if nwd(T[y][x],T[y][new_x])==1:
                best_path=min(best_path,rook(T,new_x,y,target,going_left)+1)
    for new_y in range(y+1,n):
        if nwd(T[y][x],T[new_y][x])==1:
            best_path=min(best_path,rook(T,x,new_y,target,going_left)+1)
    return best_path

def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

n=int(input())
T=[[randint(2,99) for _ in range(n)] for _ in range(n)]
print(btr_race(T))
print(*T,sep='\n')
