def liczby_wp(N,a=0,b=0,cnt_a=0,cnt_b=0):
    if N==0:
        if a!=0 and b!=0 and nwd(a,b)==1:
            print(a,b)
            return 1
        return 0
    return liczby_wp(N//10,a+(N%10)*(10**cnt_a),b,cnt_a+1,cnt_b)+liczby_wp(N//10,a,b+(N%10)*(10**cnt_b),cnt_a,cnt_b+1)

def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

n=int(input())
print(liczby_wp(n))
