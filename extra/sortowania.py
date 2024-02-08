import time
from random import randint

def InsertionSort(T):
    n=len(T)
    for i in range(1,n):
        x=T[i]
        j=i-1
        while j>=0 and x<T[j]:
            T[j+1]=T[j]
            j-=1
        T[j+1]=x

def InsertionSort2(T):
    n=len(T)
    for i in range(2,n):
        x=T[i]
        lewy=1
        prawy=i-1
        while lewy<=prawy:
            sr=(lewy+prawy)//2
            if x<T[sr]:
                prawy=sr-1
            else:
                lewy=sr+1
        for j in range(i-1,lewy-1,-1):
            T[j+1]=T[j]
        T[lewy]=x

def SelectionSort(T):
    n=len(T)
    for i in range(n-1):
        mn=i
        for j in range(i+1,n):
            if T[j]<T[mn]:
                mn=j
        T[mn],T[i]=T[i],T[mn]

def BubbleSort(T):
    n=len(T)
    for i in range(1,n):
        for j in range(n-1,i-1,-1):
            if T[j-1]>T[j]:
                T[j-1],T[j]=T[j],T[j-1]

def CombSort(T):
    swapped=True
    n=len(T)
    gap=n
    while gap>1 or swapped:
        gap=max(int(gap/1.3),1)
        top=n-1-gap
        swapped=False
        for i in range(top+1):
            j=i+gap
            if T[i]>T[j]:
                T[i],T[j]=T[j],T[i]
                swapped=True

def QuickSort1(T,l,p):
    i=l
    j=p
    x=T[(l+p)//2]
    while i<=j:
        while T[i]<x:
            i+=1
        while T[j]>x:
            j-=1
        if i<=j:
            T[j],T[i]=T[i],T[j]
            i+=1
            j-=1
    if l<j:
        QuickSort1(T,l,j)
    if p>i:
        QuickSort1(T,i,p)

"""def QuickSort2(T):
    n=len(T)
    stos=[]
    stos.append((0,n-1))
    while len(stos)>0:
        l,p=stos.pop()
        i=l
        j=p
        x=T[(l+p)//2]
        while i<=j:
            while T[i]<x:
                i+=1
            while T[j]>x:
                j-=1
            if i<=j:
                T[j],T[i]=T[i],T[j]
                i+=1
                j-=1
            if l<j:
                stos.append((l,j))
            if p>i:
                stos.append((i,p))"""

T0=[randint(1,100000) for _ in range(10000)]
T1=T0[::]
T2=T0[::]
T3=T0[::]
T4=T0[::]
T5=T0[::]
T6=T0[::]
print("Przed posortowaniem:")
print(*T0[:10],'\n')
a=time.time()
InsertionSort(T0)
b=time.time()
print("Po posortowaniu:")
print(*T0[:20])
print(b-a,'\n\n')
print("Przed posortowaniem:")
print(*T1[:10],'\n')
a=time.time()
SelectionSort(T1)
b=time.time()
print("Po posortowaniu:")
print(*T1[:20])
print(b-a,'\n\n')
print("Przed posortowaniem:")
print(*T2[:10],'\n')
a=time.time()
SelectionSort(T2)
b=time.time()
print("Po posortowaniu:")
print(*T2[:20])
print(b-a,'\n\n')
print("Przed posortowaniem:")
print(*T3[:10],'\n')
a=time.time()
BubbleSort(T3)
b=time.time()
print("Po posortowaniu:")
print(*T3[:20])
print(b-a,'\n\n')
print("Przed posortowaniem:")
print(*T4[:10],'\n')
a=time.time()
CombSort(T4)
b=time.time()
print("Po posortowaniu:")
print(*T4[:20])
print(b-a,'\n\n')
print("Przed posortowaniem:")
print(*T5[:10],'\n')
a=time.time()
QuickSort1(T5,0,9999)
b=time.time()
print("Po posortowaniu:")
print(*T5[:20])
print(b-a,'\n\n')
#zadziwiająco długo...
"""print("Przed posortowaniem:")
print(*T6[:10],'\n')
k=time.time()
QuickSort2(T6)
l=time.time()
print("Po posortowaniu:")
print(*T6[:20])
print(l-k,'\n\n')"""
