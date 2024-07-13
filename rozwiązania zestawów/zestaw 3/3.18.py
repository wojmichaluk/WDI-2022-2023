from random import randint

def length(T):
    n=len(T)
    longest=0
    for x in range(n):
        for y in range(x+1,n):
            flag=True
            for i in range(y-x+1):
                if T[x+i]!=T[y-i] or T[x+i]%2==0:
                    flag=False
                    break
            if flag:
                longest=max(longest,y-x+1)
    return longest

#sztywny przypadek dla N=20
#N=int(input())
N=20
T=[randint(1,10) for _ in range(N)]
print(length(T))
