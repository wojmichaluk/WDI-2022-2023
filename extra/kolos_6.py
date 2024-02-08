def A(x):
    return x+3
def B(x):
    return 2*x
def C(x):
    n=1
    while x//10**(n-1)>0:
        if ((x%10**n)//10**(n-1))%2==0:
            x+=10**(n-1)
        n+=1
    return x

def zliczanie(x,y,n,ost=''):
    if x==y:
        return 1
    if n==0:
        return 0
    suma1=suma2=suma3=suma4=0
    if ost=='A':
        suma1=zliczanie(B(x),y,n-1,"B")+zliczanie(C(x),y,n-1,"C")
    elif ost=='B':
        suma2=zliczanie(A(x),y,n-1,"A")+zliczanie(C(x),y,n-1,"C")
    elif ost=='C':
        suma3=zliczanie(A(x),y,n-1,"A")+zliczanie(B(x),y,n-1,"B")
    else:
        suma4=zliczanie(A(x),y,n-1,"A")+zliczanie(B(x),y,n-1,"B")+zliczanie(C(x),y,n-1,"C")
    return suma1+suma2+suma3+suma4

x=int(input())
y=int(input())
n=int(input())
print(zliczanie(x,y,n))
