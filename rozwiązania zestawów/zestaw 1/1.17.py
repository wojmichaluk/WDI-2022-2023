eps=1e-8
def iloraz(x1,x2):
    x3=x1+x2
    while abs(x2/x1-x3/x2)>eps:
        x1=x2
        x2=x3
        x3=x1+x2
    print(x3/x2)
print('Wartość, do której dąży iloraz kolejnych wyrazów ciągu')
print('Fibonacciego w zależności od wartości dwóch początkowych wyrazów:')
for i in range(1,11):
    for j in range(1,11):
        print('x1=',i,'x2=',j,end='\t')
        iloraz(i,j)
