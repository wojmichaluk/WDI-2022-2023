def liczba_krokow(x):
    kroki=0
    while x!=1:
        x=(x%2)*(3*x+1)+(1-x%2)*x/2
        kroki+=1
    return kroki
maks=wyraz=0
for i in range(2,10001):
    j=liczba_krokow(i)
    if j>maks:
        maks=j
        wyraz=i
print(wyraz)
