from random import randint

def longest(T):
    longest=0
    last=0
    current=0
    for t in T:
        if t>last:
            current+=1
        else:
            if current>longest:
                longest=current
            current=1
        last=t
    return longest

N=int(input())
T=[randint(1,1000) for _ in range(N)]
print(longest(T))
