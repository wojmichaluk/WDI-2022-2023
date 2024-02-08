T=[None for _ in range(32)]
while(True):
    b=int(input())
    for i in range(31,-1,-1):
        T[i]=b%2
        b/=2
    print(T[0],end=' ')
    for i in range(9):
        print(T[i],end=' ')
    for i in range(9,32):
        print(T[i])
