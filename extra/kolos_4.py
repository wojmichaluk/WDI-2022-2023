def evenOnesInBinary(n):
    count=0
    while n>0:
        count+=n%2
        n//=2
    return count%2

def czy_da_sie_usunac(T):
    n=len(T)
    tab=[[evenOnesInBinary(T[i][j]) for i in range(n)] for j in range(n)]
    for w in range(n):
        for k1 in range(n):
            for k2 in range(n):
                if k1==k2:
                    continue
                for i in range(n):
                    if suma(tab,w,k1,k2):
                        return True
    return False

def suma(T,a,b,c):
    n=len(T)
    for i in range(n):
        for j in range(n):
            if i!=a and j!=b and j!=c:
                if T[i][j]==0:
                    return False
    return True

#T=[[2,1,1,1],[1,3,1,1],[1,1,3,1],[1,1,1,3]]
#print(czy_da_sie_usunac(T))
