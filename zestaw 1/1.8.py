def czy_pierwsza(x):
    if x==0 or x==1:
        return False
    elif x==2:
        return True
    elif x%2==0:
        return False
    else:
        i=3
        while i*i<=x:
            if x%i==0:
                return False
            i+=2
        return True

for i in range(5):
    num=int(input())
    if czy_pierwsza(num):
        print("TAK")
    else:
        print("NIE")
