def binary_cut(T,ind,power=0,curr=0):
    if ind==-1 or power==30:
        return False
    curr+=T[ind]*2**power
    print(curr,ind,T[ind])
    if is_prime(curr):
        if ind==0:
            return True
        return binary_cut(T,ind-1) or binary_cut(T,ind-1,power+1,curr)
    else:
        return binary_cut(T,ind-1,power+1,curr)

def is_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        i=3
        while i*i<=n:
            if n%i==0:
                return False
            i+=2
        return True

#T=[1,1,1,0,1,1]
#print(binary_cut(T,len(T)-1))
