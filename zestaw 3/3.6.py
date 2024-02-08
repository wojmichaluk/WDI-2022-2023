def odd_digit(x):
    while x>0:
        if x%10 in [1,3,5,7,9]:
            return True
        x//=10
    return False

#zakładamy, że N=1000
T=[_+1 for _ in range(1000)]
for t in T:
    print(t,odd_digit(t))
