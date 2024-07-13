def suma_dzielnikow(x):
    i=1
    suma=0
    while i*i<x:
        if x%i==0:
            suma+=i+x//i
        i+=1
    if i*i==x:
        suma+=i
    return suma-x
for i in range(1,1000000):
    j=suma_dzielnikow(i)
    if j<1000000 and j>i and suma_dzielnikow(j)==i:
        print(i,'i',j)


