from random import random,randint

def distance(P):
    suma_x=suma_y=suma_z=0
    for punkt in P:
        suma_x+=punkt[0]
        suma_y+=punkt[1]
        suma_z+=punkt[2]
    x=suma_x/len(P)
    y=suma_y/len(P)
    z=suma_z/len(P)
    return (x**2+y**2+z**2)**0.5

def closer_than_r(T,r,P=[],i=0):
    if len(P)>=3:
        if distance(P)<=r:
            return True
    if i==len(T):
        return False
    return closer_than_r(T,r,P,i+1) or closer_than_r(T,r,P+[T[i]],i+1)

n=int(input())
r=float(input())
T=[(50*(-1)**randint(1,2)*random(),50*(-1)**randint(1,2)*random(),50*(-1)**randint(1,2)*random()) for _ in range(n)]
print(closer_than_r(T,r))
