def przenies(a,b,n):
    p=6-a-b
    if n==1:
        print("Przestaw krążek ",n," ze słupka ",a," na słupek ",b)
    else:
        przenies(a,p,n-1)
        print("Przestaw krążek ",n," ze słupka ",a," na słupek ",b)
        przenies(p,b,n-1)

n=int(input())
przenies(1,2,n)
