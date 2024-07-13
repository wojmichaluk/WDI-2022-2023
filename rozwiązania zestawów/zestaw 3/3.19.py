def sp_pod(T):
    l=1
    longest=0
    suma_el=T[0]
    suma_ind=0
    last=T[0]
    for i in range(1,N):
        if T[i]>last:
            l+=1
            suma_el+=T[i]
            suma_ind+=i
            if suma_el==suma_ind:
                if l>longest:
                    longest=l
        else:
            suma_el=T[i]
            suma_ind=i
            l=1
        last=T[i]
    if longest<2:
        return 0
    else:
        return longest

#sztywny przypadek dla N=5 
N=5
T=[5,0,2,4,7]
print(sp_pod(T))
