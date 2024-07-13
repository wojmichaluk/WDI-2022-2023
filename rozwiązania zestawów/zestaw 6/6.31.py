s=0

def suma_il(divisors,i=0,il=1):
    if i==len(divisors):
        if il!=1:
            global s
            s+=il
        return
    suma_il(divisors,i+1,il)
    suma_il(divisors,i+1,il*divisors[i])

def div(n):
    i=2
    j=0
    divs=[-1]*20
    while n>1:
        if n%i==0:
            divs[j]=i
            j+=1
            while n%i==0:
                n//=i
        i+=1
    return divs[:j]

n=int(input())
suma_il(div(n))
print(s)
