L=input().split()
n=int(L[0])
m=int(L[1])
num=int((n*10**(2*m))**(0.5))
suma=0
while num>1:
    suma+=num%10
    num//=10
print(suma)
