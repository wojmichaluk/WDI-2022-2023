num=int(input())
a,b=0,1
suma=0
while suma<num:
    suma+=b
    b+=a
    a=b-a
a,b=0,1
while suma>num:
    suma-=b
    b+=a
    a=b-a
print(suma==num)
