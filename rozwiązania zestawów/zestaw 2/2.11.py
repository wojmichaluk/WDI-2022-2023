n=int(input())
last=10
while n>0 and last>n%10:
    last=n%10
    n//=10
print(n==0)
        
