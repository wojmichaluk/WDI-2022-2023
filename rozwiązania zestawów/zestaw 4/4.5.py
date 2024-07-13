from random import randint

def highest(T):
    l_wp=l_wm=h_kp=h_km=0
    suma=0
    for element in T[0]:
        suma+=element
    if suma<0:
        lowest_m=suma
        lowest_p=0
    elif suma>0:
        lowest_m=0
        lowest_p=suma
    else:
        lowest_m=lowest_p=0
    for i in range(1,N):
        suma=0
        for element in T[i]:
            suma+=element
        if suma>0 and lowest_p==0:
            lowest_p=suma
            l_wp=i
        elif suma>0 and suma<lowest_p:
            lowest_p=suma
            l_wp=i
        elif suma<0 and lowest_m==0:
            lowest_m=suma
            l_wm=i
        elif suma<0 and suma>lowest_m:
            lowest_m=suma
            l_wm=i
    suma=0
    for i in range(N):
        suma+=T[i][0]
    if suma<0:
        highest_m=suma
        highest_p=0
    elif suma>0:
        highest_m=0
        highest_p=suma
    else:
        highest_m=highest_p=0
    for i in range(1,N):
        suma=0
        for j in range(N):
            suma+=T[j][i]
        if suma>0 and suma>highest_p:
            highest_p=suma
            h_kp=i
        elif suma<0 and suma<highest_m:
            highest_m=suma
            h_km=i
    if lowest_m==0 and lowest_p==0:
        return -1,-1
    elif lowest_m==0:
        return l_wp,h_kp
    elif lowest_p==0:
        return l_wm,h_km
    else:
        if highest_p/lowest_p>highest_m/lowest_m:
            return l_wp,h_kp
        else:
            return l_wm,h_km

N=int(input())
T=[[randint(-9,9) for _ in range(N)] for _ in range(N)]
print(highest(T))
