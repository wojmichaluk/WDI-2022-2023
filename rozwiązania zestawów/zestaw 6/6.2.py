def waga(n):
    suma=0
    k=2
    while n>1:
        if n%k==0:
            suma+=1
            while n%k==0:
                n//=k
        k+=1
    return suma

def podzial(T,s1=0,s2=0,s3=0,i=0):
    if i==len(T):
        return s1==s2==s3
    x=waga(T[i])
    return podzial(T,s1+x,s2,s3,i+1) or podzial(T,s1,s2+x,s3,i+1) or podzial(T,s1,s2,s3+x,i+1)

#T=[2,3,5,7,11]
#print(podzial(T))
