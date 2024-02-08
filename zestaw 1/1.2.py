def fib(x1,x2):
    x3=x1+x2
    while x1<2022:
        x1=x2
        x2=x3
        x3=x1+x2
    if x1==2022:
        return True
    else:
        return False

min_sum=200
for a in range(1,100):
    for b in range(1,100):
        if fib(a,b):
            if a+b<min_sum:
                min_sum=a+b
print("suma:",min_sum)
