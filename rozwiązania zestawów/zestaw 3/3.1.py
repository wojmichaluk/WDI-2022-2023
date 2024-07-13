def zam(n,b):
    T=[0 for _ in range(64)]
    i=0
    while n>0:
        T[i]=n%b
        n//=b
        i+=1
    for j in range(i-1,-1,-1):
        print("0123456789ABCDEF"[T[j]],end='')
n=int(input())
b=int(input())
zam(n,b)
