from random import random,randint

def distance(P):
    suma_x=suma_y=0
    for punkt in P:
        suma_x+=punkt[0]
        suma_y+=punkt[1]
    x=suma_x/len(P)
    y=suma_y/len(P)
    return (x**2+y**2)**0.5

def closer_than_r(T,r,k,P=[],i=0):
    if len(P)>0 and len(P)%3==0 and len(P)<k:
        if distance(P)<=r:
            return True
    if i==len(T) or len(P)>=k:
        return False
    return closer_than_r(T,r,k,P,i+1) or closer_than_r(T,r,k,P+[T[i]],i+1)

n=int(input())
r=float(input())
k=int(input())
T=[(50*(-1)**randint(1,2)*random(),50*(-1)**randint(1,2)*random()) for _ in range(n)]
print(closer_than_r(T,r,k))
