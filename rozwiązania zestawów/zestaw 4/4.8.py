from random import randint

def geo(T):
    if N<3:
        return False,0
    longest=2
    for j in range(N-2):
        current=2
        last=T[N-2-j][1]
        q=last/T[N-3-j][0]
        for i in range(3,N+1-j):
            if T[N-i-j][i-j-1]/last!=q:
                longest=max(longest,current)
                current=2
                q=T[N-i-j][i-j-1]/last
            else:
                current+=1
            last=T[N-i-j][i-j-1]
        longest=max(longest,current)
    for j in range(N-3):
        current=2
        last=T[1][2+j]
        q=last/T[0][1+j]
        for i in range(1,N-2-j):
            if T[1+i][2+i+j]/last!=q:
                longest=max(longest,current)
                current=2
                q=T[1+i][2+i+j]/last
            else:
                current+=1
            last=T[1+i][2+i+j]
        longest=max(longest,current)
    if longest==2:
        return False,0
    else:
        return True,longest

N=int(input())
T=[[randint(1,8) for _ in range(N)] for _ in range(N)]
print(geo(T))
