def czy_doskonala(x):
    if x==0 or x==1:
        return False
    else:
        i=1
        suma=0
        while i*i<x:
            if x%i==0:
                suma+=i+x//i
            i+=1
        if i*i==x:
            suma+=i
        if suma==2*x:
            return True
        else:
            return False
for i in range(1000000):
    if czy_doskonala(i):
        print(i)
print("KONIEC")
