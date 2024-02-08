from random import randint

def cheapest(T,k,w=0):
    if w==7:
        return T[w][k]
    if k>0:
        left=cheapest(T,k-1,w+1)
    else:
        left=float('inf')
    if k<7:
        right=cheapest(T,k+1,w+1)
    else:
        right=float('inf')
    middle=cheapest(T,k,w+1)
    return min(left,right,middle)+T[w][k]

k=int(input())
while k<0 or k>7:
    k=int(input())
T=[[randint(1,9) for _ in range(8)] for _ in range(8)]
print(cheapest(T,k))
#for i in range(8):
    #print(T[i])
