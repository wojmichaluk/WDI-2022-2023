def suma_eq(T,ind=0,suma=0,s_ind=0,moc=0):
    global maks_moc
    if suma==s_ind and 0<moc<maks_moc:
        maks_moc=moc
        return suma  
    if ind==len(T):
        return float('inf')
    return min(suma_eq(T,ind+1,suma,s_ind,moc),suma_eq(T,ind+1,suma+T[ind],s_ind+ind,moc+1))

T=[1,7,3,5,11,2]
maks_moc=len(T)
print(suma_eq(T))
