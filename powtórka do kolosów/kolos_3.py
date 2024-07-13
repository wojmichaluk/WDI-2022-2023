def transform(x,y,n):
    suma=0
    for i in range(4**n):
        kopia=x
        quad=toQuadWOZero(i)
        if not isDouble(quad):
            continue
        for j in range(len(quad)):
            if quad[j]=='1':
                kopia=A(kopia)
            elif quad[j]=='2':
                kopia=B(kopia)
            elif quad[j]=='3':
                kopia=C(kopia)
        if kopia==y:
            suma+=1
            print(quad)
    return suma

def A(n):
    return n+3

def B(n):
    return 2*n

def C(n):
    x=str(n)
    for i in range(len(x)):
        if int(x[i])%2==0:
            x=x[:i]+str(int(x[i])+1)+x[i+1:]
    return int(x)

def isDouble(quad):
    last='5'
    for i in range(len(quad)):
        if quad[i]==last:
            return False
        if quad[i]!='0':
            last=quad[i]
    return True

def toQuadWOZero(n):
    num=n
    s=''
    while num>0:
        m=num%4
        if m==0:
            return '0'
        s+=str(m)
        num//=4
    return s[-1::-1]
    
X=int(input())
Y=int(input())
N=int(input())
print(transform(X,Y,N))
