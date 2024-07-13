from math import log

def f(x):
    return x**x-2022

def f_p(x):
    return (x**x)*(log(x)+1)

eps=1e-10
n=4
while abs(f(n))>eps:
    a,b=f(n),f_p(n)
    n-=a/b
print(n)
        
