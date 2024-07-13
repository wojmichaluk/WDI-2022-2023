from random import randint

def longest(T):
    i,j=0,0
    curr_len,max_len=1,1
    curr_product=T[0]
    while j!= len(T)-1:
        if is_valid(T[j+1],curr_product):
            curr_product*=T[j+1]
            j+=1
            curr_len+=1
            if curr_len>max_len:
                max_len=curr_len
        else:
            if curr_product==1:
                i+=1
                j+=1
            else:
                curr_product//=T[i]
                i+=1
                curr_len-=1
    return max_len

def is_valid(n,product):
    if product%n==0:
        return False
    divisor=2
    divided=False
    while n>1:
        if n%divisor==0:
            n//=divisor
            if product%divisor==0 or divided:
                return False
            divided=True
        else:
            divisor+=1
            divided=False
    return True

#sztywny przypadek dla N=20
#N=int(input())
N=20
T=[randint(1,999) for _ in range(N)]
#T=[2,23,33,35,7,4,6,7,5,11,13,22]
print(longest(T))
