from math import log10

def A(x):
    if get_leng(x)<2:
        return x
    y=x//100
    d1=x%10
    d2=(x%100)//10
    return y*100+d1*10+d2

def B(x):
    return x*3

def C(x):
    if get_leng(x)<2:
        return x
    return x%(10**(get_leng(x)-1))

def get_leng(x):
    return int(log10(x))+1

def op(x,y,seq,i=0):
    if x==y:
        return seq
    if i>=7:
        return ""
    seq[i]='A'
    res=op(A(x),y,seq,i+1)
    if res!="":
        return res
    seq[i]='B'
    res=op(B(x),y,seq,i+1)
    if res!="":
        return res
    seq[i]='C'
    res=op(C(x),y,seq,i+1)
    if res!="":
        return res
    seq[i]=""
    return ""

x=int(input())
y=int(input())
print(op(x,y,[""]*7))
