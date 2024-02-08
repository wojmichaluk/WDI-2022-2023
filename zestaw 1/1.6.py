import math

eps=1e-10
a=0
b=10
while b-a>eps:
    c=0.5*(a+b)
    if math.exp(c*math.log(c))-2022>0:
        b=c
    else:
        a=c
print(a)
