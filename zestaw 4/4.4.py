from random import randint

def highest(T):
    l_w=h_k=0
    suma=0
    for element in T[0]:
        suma+=element
    lowest=suma
    for i in range(1,N):
        suma=0
        for element in T[i]:
            suma+=element
        if suma<lowest:
            lowest=suma
            l_w=i
    suma=0
    for i in range(N):
        suma+=T[i][0]
    highest=suma
    for i in range(1,N):
        suma=0
        for j in range(N):
            suma+=T[j][i]
        if suma>highest:
            highest=suma
            h_k=i
    return l_w,h_k

N=int(input())
T=[[randint(1,999) for _ in range(N)] for _ in range(N)]
print(highest(T))
