from random import randint

def odszukaj(T):
    n=len(T)
    for w in range(n):
        for k in range(n):
            if w>=2:
                if T[w][k]+T[w-1][k]==T[w-2][k] and w_ciagu(T[w][k],T[w-1][k]):
                    return dlugosc(T,k,w-3,0,1)
            if w<=n-3:
                if T[w][k]+T[w+1][k]==T[w+2][k] and w_ciagu(T[w][k],T[w+1][k]):
                    return dlugosc(T,k,w+3,n-1,2)
            if k>=2:
                if T[w][k]+T[w][k-1]==T[w][k-2] and w_ciagu(T[w][k],T[w][k-1]):
                    return dlugosc(T,k-3,w,0,3)
            if k<=n-3:
                if T[w][k]+T[w][k+1]==T[w][k+2] and w_ciagu(T[w][k],T[w][k+1]):
                    return dlugosc(T,k+3,w,n-1,4)

def dlugosc(T,k,w,lim,flag):
    dlug=3
    if flag==1:
        while w>=lim:
            if T[w+2][k]+T[w+1][k]==T[w][k]:
                dlug+=1
            else:
                break
            w-=1
    elif flag==2:
        while w<=lim:
            if T[w-2][k]+T[w-1][k]==T[w][k]:
                dlug+=1
            else:
                break
            w+=1
    elif flag==3:
        while k>=lim:
            if T[w][k+2]+T[w][k+1]==T[w][k]:
                dlug+=1
            else:
                break
            k-=1
    elif flag==4:
        while k<=lim:
            if T[w][k-2]+T[w][k-1]==T[w][k]:
                dlug+=1
            else:
                break
            k+=1
    return dlug

def w_ciagu(a,b):
    if a>b:
        return False
    x,y=1,1
    while x<=a and y<=b:
        if a==x and b==y:
            return True
        x,y=y,x+y
    return False

T=[[randint(1,9) for _ in range(8)] for _ in range(8)]
print(odszukaj(T))
print(*T,sep='\n')
