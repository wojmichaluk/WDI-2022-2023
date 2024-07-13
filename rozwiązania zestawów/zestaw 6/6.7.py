def waga(T,i,r):
    n=len(T)
    if r==0:
        return True
    if r<0 or i>n-1:
        return False
    return waga(T,i+1,r) or waga(T,i+1,r-T[i])

#przykładowe odważniki
odw=[1,3,6,10,16,24]
for i in range(1,61):
    print(i,waga(odw,0,i))
