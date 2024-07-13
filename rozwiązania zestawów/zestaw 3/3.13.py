from random import randint

def longest(T):
    for i in range(N,0,-1):
        for j in range(N-i+1):
            J=T[j:j+i]
            for k in range(N-i+1):
                K=T[k+i-1:k-1:-1]
                if J==K:
                    return i

N=int(input())
T=[randint(100,999) for _ in range(N)]
#T=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
#N=15
print(longest(T))
