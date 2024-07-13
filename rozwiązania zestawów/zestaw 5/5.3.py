def checking(T):
    n=len(T)
    rows=[queen[0] for queen in T]
    cols=[queen[1] for queen in T]
    for queen in T:
        w=queen[0]
        k=queen[1]
        w_c=k_c=0
        for row in rows:
            if w==row:
                w_c+=1
            if w_c==2:
                return False
        for col in cols:
            if k==col:
                k_c+=1
            if k_c==2:
                return False
        for i in range(1,min(w,k)+1):
            if (w-i,k-i) in T:
                return False
        for i in range(1,n-max(w,k)):
            if (w+i,k+i) in T:
                return False
        for i in range(1,min(min(w,k)+1,n-max(w,k))):
            if (w-i,k+i) in T:
                return False
        for i in range(1,min(max(w,k)+1,n-min(w,k))):
            if (w+i,k-i) in T:
                return False
    return True

#T=[(1,1),(15,32),(99,98)]
#print(checking(T))
