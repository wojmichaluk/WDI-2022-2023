from random import randint

def trojki(T):
    count=0
    for i in range(N-2):
        for j in range(i+1,min(N-1,i+3)):
            for k in range(j+1,min(N,j+3)):
                if NWD(T[i],T[j],T[k])==1:
                    count+=1
    return count

def NWD(x,y,z):
    while y!=0:
        temp=y
        y=x%y
        x=temp
    while z!=0:
        temp=z
        z=x%temp
        x=temp
    return x

#sztywny przypadek dla N=20
#N=int(input())
N=20
T=[0 for _ in range(N)]
i=0
for i in range(N):
    temp=randint(1,99)
    while temp in T:
        temp=randint(1,99)
    T[i]=temp
print(trojki(T))
