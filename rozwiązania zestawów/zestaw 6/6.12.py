from random import randint

ilosc=0

def enki_tab(T,multi,ile,i=0,tab=[]):
    global ilosc
    if ile==1:
        for j in range(i,len(T)):
            if T[j]==multi:
                ilosc+=1
                tab2=tab+[T[j]]
                print(*tab2)
    else:
        for j in range(i,len(T)-ile+1):
            if multi%T[j]==0:
                enki_tab(T,multi//T[j],ile-1,j+1,tab+[T[j]])

N=int(input())
n=int(input())
while n>N:
    n=int(input())
iloczyn=int(input())
T=[randint(1,9) for _ in range(N)]
print(*T)
enki_tab(T,iloczyn,n)
print(ilosc)
