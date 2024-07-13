F=[1,1]
n=int(input())
if n==1:
    print("True")
else:
    i=2
    while F[i-1]<n:
        F.append(F[i-1]+F[i-2])
        i+=1
    check=False
    for j in range(i):
        for k in range(j+1,i):
            if F[j]*F[k]==n:
                check=True
                break
        if check: break
    print(check)
