def odwaz(T,waga,i=0):
    if waga==0:
        return True
    elif i==len(T):
        return False
    if odwaz(T,waga,i+1):
        return True
    if odwaz(T,waga-T[i],i+1):
        print(T[i],end=' ')
        return True
    if odwaz(T,waga+T[i],i+1):
        print(-1*T[i],end=' ')
        return True
    return False

#przykładowe odważniki
odw=[1,3,6,10,16,24]
for i in range(1,61):
    print(i,sep='')
    odwaz(odw,i)
    print()
