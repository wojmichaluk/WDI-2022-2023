def dziel(a,b,n):
    a,b=skroc(a,b)
    print(a//b,end='')
    a%=b
    print('.',end='')
    for _ in range(n):
        a*=10
        print(a//b,end='')
        a%=b
    print()
    
def skroc(a,b):
    old_a,old_b=a,b
    while b!=0:
        a,b=b,a%b
    return old_a//a,old_b//a

a=int(input())
b=int(input())
n=int(input())
dziel(a,b,n)
