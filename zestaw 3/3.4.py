def Euler(n):
    digits=[1]+[0]*(n+10)
    fact=k=1
    while fact<=10**(n+1):
        fact*=k
        k+=1
        long_div(1,fact,digits)
    for i in range(len(digits)-1,0,-1):
        digits[i-1]+=digits[i]//10
        digits[i]%=10
    return digits[:n+1]

def long_div(a,b,t):
    for i in range(1,len(t)):
        a*=10
        t[i]+=a//b
        a%=b
        if a==0:
            return

N=int(input())
T=Euler(N)
print(T[0],'.',sep='',end='')
T=T[1:]
for digit in T:
    print(digit,end='')

