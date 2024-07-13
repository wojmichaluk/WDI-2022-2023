from random import randint

def aryth(T):
    r=T[1]-T[0]
    current=2
    last=T[1]
    longest=0
    for i in range(2,len(T)):
        if T[i]-last!=r:
            longest=max(longest,current)
            current=2
            r=T[i]-T[i-1]
        else:
            current+=1
        last=T[i]
    longest=max(longest,current)
    if longest==2:
        return 0
    else:
        return longest

#sztywny przypadek dla N=20
#N=int(input())
N=20
T=[randint(1,9) for _ in range(N)]
print(aryth(T))

