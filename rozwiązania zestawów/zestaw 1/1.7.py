x1=x2=1
x3=x1+x2
num=int(input())
mul=1
check=False
while x1**2<=num:
    if num==mul:
        check=True
        break
    x1=x2
    x2=x3
    x3=x1+x2
    mul=x1*x2
if check:
    print("TAK")
else:    
    print("NIE")
    
