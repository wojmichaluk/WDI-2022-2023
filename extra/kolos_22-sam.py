from random import randint

def nieparzyste_w_siodemkowym(n):
    cnt=0
    while n>0:
        if (n%7)%2==1:
            cnt+=1
        n//=7
    return cnt

def czy_mozliwe(tab1,tab2):
    MAX1=len(tab1)
    MAX2=len(tab2)
    for i in range(MAX1):
        for j in range(MAX1):
            tab1[i][j]=nieparzyste_w_siodemkowym(tab1[i][j])
    for i in range(MAX2):
        for j in range(MAX2):
            tab2[i][j]=nieparzyste_w_siodemkowym(tab2[i][j])
    for w in range(MAX2-MAX1+1):
        for k in range(MAX2-MAX1+1):
            zgodne=0
            for i in range(MAX1):
                for j in range(MAX1):
                    if tab1[i][j]==tab2[i+w][j+k]:
                        zgodne+=1
            if zgodne>=0.33*MAX1*MAX1:
                return True
    return False

T1=[[randint(1,1000) for _ in range(20)] for _ in range(20)]
T2=[[randint(1,1000) for _ in range(32)] for _ in range(32)]
#print(*T1,sep='\n')
#print(*T2,sep='\n')
print(czy_mozliwe(T1,T2))
#print(*T1,sep='\n')
#print(*T2,sep='\n')
