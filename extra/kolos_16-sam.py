def A(x):
    return x+3

def B(x):
    return 2*x

def C(x):
    new_num=0
    power=0
    while x>0:
        digit=x%10
        if digit%2!=0:
            digit-=1
        new_num=digit*10**power+new_num
        x//=10
        power+=1
    return new_num

def przeksztalc(x,y,n):
    def rek(x,y,n,i=0,last=''):
        if x==y:
            return i
        if i==n:
            return float('inf')
        ciag1=ciag2=ciag3=float('inf')
        if last!='A':
            ciag1=rek(A(x),y,n,i+1,'A')
        if last!='B':
            ciag2=rek(B(x),y,n,i+1,'B')
        if last!='C':
            ciag3=rek(C(x),y,n,i+1,'C')
        return min(ciag1,ciag2,ciag3)
    a=rek(x,y,n)
    if a>n:
        return -1
    return a

#print(przeksztalc(23,39,4))
