n=int(input())
a=2
if n%2!=0:
    a=7
    while a<n and n%a!=0:
        a=a*9+4
print(n%a==0)
