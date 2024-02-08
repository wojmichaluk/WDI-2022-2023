from random import randint

occ=0
al=1000
for n in range(20,41):
    for i in range(al):
        T=[False for _ in range(365)]
        for j in range(n):
            temp=randint(1,365)
            if T[temp-1]:
                occ+=1
                break
            else:
                T[temp-1]=True
    print(n,occ/al)
    occ=0
