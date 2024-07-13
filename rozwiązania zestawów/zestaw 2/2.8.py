n=int(input())
for i in range(n+1,1001):
    a,b=0,1
    suma=0
    while suma<i:
        suma+=b
        b+=a
        a=b-a
    a,b=0,1
    while suma>i:
        suma-=b
        b+=a
        a=b-a
    if suma!=i:
        print(i)
        break
