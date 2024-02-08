def NWD(x,y):
    while y!=0:
        temp=y
        y=x%y
        x=temp
    return x
a=int(input())
b=int(input())
c=int(input())
d=NWD(a,b)
e=NWD(d,c)
print(e)
