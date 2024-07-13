def square(T):
    n=len(T)
    xs=[pt[0] for pt in T]
    ys=[pt[1] for pt in T]
    for i in range(n):
        for j in range(i+1,n):
            if xs[i]==xs[j]:
                pt1=T[i]
                pt2=T[j]
                bok=abs(pt1[1]-pt2[1])
                if (pt1[0]+bok,pt1[1]) in T and (pt2[0]+bok,pt2[1]) in T:
                    flag=True
                    for cord in T:
                        if between(pt1[0],pt1[0]+bok,cord[0]) and between(pt1[1],pt2[1],cord[1]):
                            flag=False
                            break
                    if flag:
                        return True
                elif (pt1[0]-bok,pt1[1]) in T and (pt2[0]-bok,pt2[1]) in T:
                    flag=True
                    for cord in T:
                        if between(pt1[0],pt1[0]-bok,cord[0]) and between(pt1[1],pt2[1],cord[1]):
                            flag=False
                            break
                    if flag:
                        return True
    return False

def between(a,b,c):
    if a>b:
        return b<c<a
    else:
        return a<c<b

#T=[(0,0),(0,3),(3,0),(3,3),(5,7)]
#print(square(T))
