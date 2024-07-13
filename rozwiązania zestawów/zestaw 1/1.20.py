x=a=float(input())
y=b=float(input())
eps=1e-8
c=(a*b)**0.5
d=(a+b)/2.0
while d-c>eps:
    a=c
    b=d
    c=(a*b)**0.5
    d=(a+b)/2.0
print("Średnia arytmetyczno-geometryczna liczb",x,'i',y,"wynosi",0.5*(c+d))
