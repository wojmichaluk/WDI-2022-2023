from random import random

def srodek_ciezkosci(T):
    suma_x=suma_y=0
    for element in T:
        suma_x+=element[0]
        suma_y+=element[1]
    return suma_x/len(T),suma_y/len(T)

def min_dist(T,i=0,P1=[],P2=[]):
    s=float('inf')
    if len(P1)>0 and len(P2)>0:
        s1=srodek_ciezkosci(P1)
        s2=srodek_ciezkosci(P2)
        s=((s1[0]-s2[0])**2+(s1[1]-s2[1])**2)**0.5
    if i==len(T):
        return s
    return min(s,min_dist(T,i+1,P1,P2),min_dist(T,i+1,P1+[T[i]],P2),min_dist(T,i+1,P1,P2+[T[i]]))

n=int(input())
T=[(100*random(),100*random()) for _ in range(n)]
print(min_dist(T))
