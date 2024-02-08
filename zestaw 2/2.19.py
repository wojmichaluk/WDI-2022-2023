def ula(a,b):
    a,b=skroc(a,b)
    print(a//b,end='')
    a%=b
    if a>0:
        print('.',end='')
        for _ in range(li25(b)):
            a*=10
            print(a//b,end='')
            a%=b
        if a>0:
            print('(',end='')
            mem=a
            while True:
                a*=10
                print(a//b,end='')
                a%=b
                if a==mem:
                    break
            print(')',end='')
    print()
def skroc(a,b):
    old_a,old_b=a,b
    while b!=0:
        a,b=b,a%b
    return old_a//a,old_b//a
def li25(b):
    i=j=0
    while b%2==0:
        b//=2
        i+=1
    while b%5==0:
        b//=5
        j+=1
    return max(i,j)
l=int(input())
m=int(input())
ula(l,m)
