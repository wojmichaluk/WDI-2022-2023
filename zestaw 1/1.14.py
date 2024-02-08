def silnia(x):
    if x==0 or x==1:
        return 1
    y=x
    while y>1:
        x*=y-1
        y-=1
    return x
eps=1e-8
def cos(x):
    suma=1
    i=1
    arg=(-1)**i*x**(2*i)/silnia(2*i)
    while abs(arg)>eps:
        suma+=arg
        i+=1
        arg=(-1)**i*x**(2*i)/silnia(2*i)
    return suma
con=0.2617993878
for i in range(25):
    print('cos(',i,'pi/12)= ',cos(con*i),sep='')
