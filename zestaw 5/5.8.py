def multi(T):
    maks=0
    for string in T:
        n=len(string)
        for i in range(1,n//2+1):
            if n%i!=0:
                continue
            if (n//i)*string[:i] in string:
                maks=max(maks,n)
    return maks

#T=["AAAAA","ABCABCABC","ABCBA","ABABABA"]
#print(multi(T))
