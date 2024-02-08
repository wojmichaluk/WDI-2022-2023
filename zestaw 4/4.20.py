from random import randint

def wieze(T):
    l=len(T)
    maks=0
    sk=[0 for _ in range(l)]
    sw=[0 for _ in range(l)]
    for i in range(l):
        for j in range(l):
            sk[i]=T[i][j]
            sw[i]=T[j][i]
    for w1 in range(l):
        for k1 in range(l):
            for w2 in range(l):
                for k2 in range(l):
                    if w1!=w2 or k1!=k2:
                        if w1==w2:
                            s=sw[w1]+sk[k1]+sk[k2]-2*T[w1][k1]-2*T[w2][k2]
                        elif k1==k2:
                            s=sw[w1]+sw[w2]+sk[k1]-2*T[w1][k1]-2*T[w2][k2]
                        else:
                            s=sw[w1]+sk[k1]+sw[w2]+sk[k2]-2*T[w1][k1]-2*T[w2][k2]-T[w1][k2]-T[w2][k1]
                        if s>maks:
                            maks=s
                            cord=(w1,k1),(w2,k2)
    """
    maks=0
    for i in range(0,l*l-1):
        for j in range(0,l*l-1):
            w1=i//l
            k1=i%l
            w2=j//l
            k2=j%l
            if w1==w2:
                s=sw[w1]+sk[k1]+sk[k2]-2*T[w1][k1]-2*T[w2][k2]
            elif k1==k2:
                s=sw[w1]+sw[w2]+sk[k1]-2*T[w1][k1]-2*T[w2][k2]
            else:
                s=sw[w1]+sk[k1]+sw[w2]+sk[k2]-2*T[w1][k1]-2*T[w2][k2]-T[w1][k2]-T[w2][k1]
            if s>maks:
                maks=s
                cord2=(w1,k1),(w2,k2)
    """
    return cord

N=int(input())
T=[[randint(1,99) for _ in range(N)] for _ in range(N)]
#print("w1={}, w2={}".format(wieze(T)))
print(wieze(T))
