from random import randint
import time

def ssp0(tab):
    n=len(tab)
    res=0
    for i in range(n):
        for j in range(i,n):
            par=0
            for k in range(i,j+1):
                par+=tab[k]
            if par>res:
                res=par
    return res

def ssp1(tab):
    n=len(tab)
    res=0
    for i in range(n):
        par=0
        for j in range(i,n):
            par+=tab[j]
            if par>res:
                res=par
    return res

def ssp2(tab,l,p):
    if l>p:
        return 0
    if l==p:
        return max(0,tab[l])
    sr=(l+p)//2
    wl=ssp2(tab,l,sr)
    wp=ssp2(tab,sr+1,p)
    sl=sp=0
    par=0
    for i in range(sr+1,p+1):
        par+=tab[i]
        if par>sp:
            sp=par
    par=0
    for i in range(sr,l-1,-1):
        par+=tab[i]
        if par>sl:
            sl=par
    return max(wl,wp,sl+sp)

def ssp3(tab):
    n=len(tab)
    par=0
    res=0
    for i in range(n):
        par+=tab[i]
        if par<0:
            par=0
        if par>res:
            res=par
    return res

#T=[1,-2,29,-17,3,-11,13,5,-7,17,-23,19,-29]
t0=time.time()
T=[randint(-20000,20000) for _ in range(10001)]
t1=time.time()
print(t1-t0)
#a=ssp0(T)
#dla 1000 elementów już liczy >8 sekund... :)
t2=time.time()
#print(a,t2-t1)
b=ssp1(T)
t3=time.time()
print(b,t3-t2)
c=ssp2(T,0,10000)
t4=time.time()
print(c,t4-t3)
d=ssp3(T)
t5=time.time()
print(d,t5-t4)
