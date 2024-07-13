eps=1e-6
S=float(input())
x=1
y=0
while abs(x-y)>eps:
    y=x
    x=0.5*(S/y+y)
print(x)
