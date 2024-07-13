from math import *

N=int(input())
T=[True for _ in range(N)]
T[0]=T[1]=False
for i in range(2,ceil(sqrt(N))):
    if T[i]:
        for j in range(i*i,N,i):
            T[j]=False
for k in range(N):
    if T[k]:
        print(k)
