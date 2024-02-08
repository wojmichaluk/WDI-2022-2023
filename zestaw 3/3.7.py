from random import randint

def only_odd_digit(x): 
    while x>0:
        if x%10 not in [1,3,5,7,9]:
            return False
        x//=10
    return True

N=int(input())
T=[randint(1,1000) for _ in range(N)]
for t in T:
    if only_odd_digit(t):
        print(True)
        break
else:
    print(False)
