n=int(input())
last=n%10
n//=10
a=10
while n>0 and a!=last:
    a=n%10
    n//=10
print(a!=last)
