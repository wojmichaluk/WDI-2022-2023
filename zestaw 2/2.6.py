n=int(input())
i=last=1
while i*i<=n:
    if n%i==0:
        last=i
    i+=1
print(n,'=',last,'*',n//last)

