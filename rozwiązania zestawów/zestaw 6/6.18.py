T=[[0 for _ in range(8)] for _ in range(8)]
"""for i in range(8):
    for j in range(8):
        T[i][j]=8*i+j+1"""

def is_on_board(x,y,n):
    return 0<=x<n and 0<=y<n

def can_choose(tab,from_x,from_y,x,y,n):
    if tab[x][y] or max(n-from_x,n-from_y)<max(n-x,n-y):
        return False
    return True

def can_move_to(from_x,from_y,x,y):
    return get_last(T[from_x][from_y])<get_first(T[x][y])

def get_first(n):
    while n//10>0:
        n//=10
    return n%10

def get_last(n):
    return n%10

def can_get_to(tab,x,y):
    if x==7 and y==7:
        return True
    for i,j in [(1,1),(1,0),(0,1),(1,-1),(0,-1),(-1,0),(-1,1)]:
        if is_on_board(x+i,y+j,8) and can_choose(tab,x,y,x+i,y+j,8) and can_move_to(x,y,x+i,y+j):
            tab[x][y]=True
            return can_get_to(tab,x+i,y+j)
        tab[x][y]=False
    return False

#for t in T:
    #print(t)
tab=[[False for _ in range(8)] for _ in range(8)]
x=int(input())
while x<0 or x>7:
    x=int(input())
y=int(input())
while y<0 or y>7:
    y=int(input())
print(can_get_to(tab,x,y))
