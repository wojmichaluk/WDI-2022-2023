T=[0 for _ in range(10)]
n=int(input())
#zakładamy, że w ciągu będzie co najmniej 10 elementów
while n!=0:
    for i in range(10):
        if n==T[i]:
            break
        if n>T[i]:
            T=T[:i]+[n]+T[i:9]
            break
    n=int(input())
print(T[9])
