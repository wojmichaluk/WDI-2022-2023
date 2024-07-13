from random import randint

#iteracyjnie
def rez(T,R):
    l=len(T)
    for i in range(l-2):
        for j in range(i+1,l-1):
            for k in range(j+1,l):
                if T[i]+T[j]+T[k]<R:
                    continue
                if T[i]+T[j]+T[k]==R:
                    return True
                if rz(rz(T[i],T[j]),T[k])>R:
                    continue
                if rz(rz(T[i],T[j]),T[k])==R:
                    return True
                if rz(T[i],T[j])+T[k]==R:
                    return True
                if rz(T[i],T[k])+T[j]==R:
                    return True
                if rz(T[k],T[j])+T[i]==R:
                    return True
                if rz(T[i],T[j]+T[k])==R:
                    return True
                if rz(T[j],T[i]+T[k])==R:
                    return True
                if rz(T[k],T[j]+T[i])==R:
                    return True                   
    return False

#rekurencyjnie
def res(T,R,w=0,Rz=0,i=0):
    if w==3:
        return Rz==R
    if i==len(T):
        return False
    if res(T,R,w,Rz,i+1):
            return True
    if res(T,R,w+1,Rz+T[i],i+1):
        return True
    if w>=1:
        if res(T,R,w+1,rz(Rz,T[i]),i+1):
            return True     
    return False

def rz(R,L):
    return (R*L)/(R+L)

n=int(input())
R=int(input())
T=[randint(1,9) for _ in range(n)]
print(rez(T,R))
print(res(T,R))
