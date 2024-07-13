from random import randint

def cut_from_tabs(t1,t2):
    n=len(t1)
    for l1 in range(1,24):
        l2=24-l1
        for j in range(n-l1+1):
            for k in range(n-l2+1):
                if czy_jest_potega(suma(t1[j:j+l1])+suma(t2[k:k+l2])):
                    return True
    return False

def suma(T):
    suma=0
    for elem in T:
        suma+=elem
    return suma

def czy_jest_potega(n):
    if n==1:
        return True
    i=2
    while i*i<=n:
        kopia_n=n
        if kopia_n%(i*i)==0:
            kopia_n//=(i*i)
            while kopia_n%i==0:
                kopia_n//=i
            if kopia_n==1:
                return True
        i+=1
    return False

t1=[randint(1,99) for _ in range(30)]
t2=[randint(1,99) for _ in range(30)]
print(cut_from_tabs(t1,t2))
