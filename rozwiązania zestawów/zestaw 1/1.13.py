def NWW(x,y):
    old_x,old_y=x,y
    while y!=0:
        temp=y
        y=x%y
        x=temp
    return old_x*old_y//x
a=int(input())
b=int(input())
c=int(input())
d=NWW(a,b)
e=NWW(d,c)
print(e)
