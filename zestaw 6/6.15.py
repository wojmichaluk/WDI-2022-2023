#ilosc=0

def hetmany(T,w=0,k=0,n=8):
    T[w][k]=1
    if n==1:
        print(*T,sep='\n')
        #global ilosc
        #ilosc+=1
        #print(ilosc)
        return
    N=len(T)
    for j in range(N):
        if can_stand(T,w+1,j):
            hetmany(T,w+1,j,n-1)
    T[w][k]=0
    return

def can_stand(T,w,k):
    moves=[(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for i in range(8):
        for j in range(1,8):
            if contains(w,k,moves[i][0],moves[i][1],j):
                if T[w+j*moves[i][0]][k+j*moves[i][1]]==1:
                    return False
    return True

def contains(w,k,w_p,k_p,j):
    return 0<=w+w_p*j<8 and 0<=k+k_p*j<8

T=[[0 for _ in range(8)] for _ in range(8)]
#for i in range(8):
    #hetmany(T,0,i,8)
#print(ilosc)
hetmany(T)
