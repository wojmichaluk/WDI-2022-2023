eps=1e-8
S=float(input())
x=1
y=0
while abs(x-y)>eps:
    y=x
    x=0.5*(S/y**2+y)
print(x)
