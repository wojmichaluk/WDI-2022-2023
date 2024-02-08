def distance(T):
    smallest=largest=0
    n=len(T[0])
    for i in range(n):
        if T[0][i]==1:
            ind=i
            break
    s_ind=l_ind=ind
    for j in range(1,n):
        for i in range(n):
            if T[j][i]==1:
                ind=i
                break
        if ind<l_ind:
            l_ind=ind
            largest=j
        elif ind==l_ind:
            for k in range(ind+1,n):
                if T[j][k]==1 and T[largest][k]==0:
                    largest=j
                    break
                elif T[j][k]==0 and T[largest][k]==1:
                    break
        if ind>s_ind:
            s_ind=ind
            smallest=j
        elif ind==s_ind:
            for k in range(ind+1,n):
                if T[j][k]==0 and T[smallest][k]==1:
                    smallest=j
                    break
                elif T[j][k]==1 and T[smallest][k]==0:
                    break
    return abs(smallest-largest)

#T=[[1,0,1,1],[1,1,1,0],[0,0,1,1],[0,1,0,1]]
#print(distance(T))
