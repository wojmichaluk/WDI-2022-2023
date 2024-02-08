def waga(T,r,i=0,w1=[],w2=[]):
    n=len(T)
    if r==0:
        print(*w1,'\t',*w2)
        return True
    if i>n-1:
        return False
    return waga(T,r,i+1,w1,w2) or waga(T,r-T[i],i+1,w1+[T[i]],w2) or waga(T,r+T[i],i+1,w1,w2+[T[i]])

#przykładowe odważniki
odw=[1,3,6,10,16,24]
for i in range(1,61):
    print(i,sep='')
    waga(odw,i)
