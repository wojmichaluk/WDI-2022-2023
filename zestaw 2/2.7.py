n=int(input())
i=1
t=i*i+i+1
while t<n and n%t!=0:
    i+=1
    t=i*i+i+1
print(n%t==0)
