eps=1e-8
def silnia(x):
    if x==0 or x==1:
        return 1
    y=x
    while y>1:
        x*=y-1
        y-=1
    return x
y=suma=0
z=1/silnia(y)
while z>eps:
    suma+=z
    y+=1
    z=1/silnia(y)
print('e=',suma)
