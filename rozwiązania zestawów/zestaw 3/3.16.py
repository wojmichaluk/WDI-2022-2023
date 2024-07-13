from random import randint

def max_min(n):
    T=[randint(-100,100) for _ in range(n)]
    biggest=smallest=T[0]
    for i in range(n):
        if T[i]>biggest:
            biggest=T[i]
        elif T[i]<smallest:
            smallest=T[i]
    bigcount=smallcount=0
    for i in range(n):
        if T[i]==biggest:
            bigcount+=1
        elif T[i]==smallest:
            smallcount+=1
        if bigcount==2 or smallcount==2:
            return False
    return True
    
n=int(input())
print(max_min(n))
