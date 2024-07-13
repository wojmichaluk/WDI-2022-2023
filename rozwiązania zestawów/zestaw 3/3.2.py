def same_digits(a,b):
    aa,bb=a,b
    T=[False for i in range(10)]
    while a>0:
        T[a%10]=True
        a//=10
    while b>0:
        if not T[b%10]:
            return False
        b//=10
    T=[False for i in range(10)]
    while bb>0:
        T[bb%10]=True
        bb//=10
    while aa>0:
        if not T[aa%10]:
            return False
        aa//=10
    return True

a=int(input())
b=int(input())
print(same_digits(a,b))
