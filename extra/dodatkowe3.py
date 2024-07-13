class Node:
    def __init__(self):
        self.next=None
        self.down=None
        #self.w=-1
        #self.k=-1

def sf(T,Tw,Tk):
    w_l=len(T)
    k_l=len(T[0])
    for r in range(w_l-1,-1,-1):
        for c in range(k_l-1,-1,-1):
            if T[r][c]:
                p=Node()
                p.next=Tw[r]
                Tw[r]=p
                p.down=Tk[c]
                Tk[c]=p

w=5
k=6
T=[[False for _ in range(k)] for _ in range(w)]
T[0][0]=T[0][2]=T[0][5]=T[1][0]=T[1][3]=T[1][5]=True
T[3][2]=T[3][3]=T[4][0]=T[4][2]=T[4][5]=True
Tw=[None for _ in range(w)]
Tk=[None for _ in range(k)]
sf(T,Tw,Tk)
print(*T,sep='\n')
#print(*Tw,sep='\n')
#print(*Tk,sep='\n')
