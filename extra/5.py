from functools import cache

@cache
def f(a,b):
    if a==0:
        return b+1
    if b==0:
        return f(a-1,1)
    return f(a-1,f(a,b-1))

for i in range(6):
    for j in range(6):
        print(i,j,f(i,j))
#liczy do f(4,0)
