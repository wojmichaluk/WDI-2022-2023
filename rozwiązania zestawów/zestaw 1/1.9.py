def podzielniki(x):
    if x==0:
        print("0 ma nieskończenie wiele dzielników")
    elif x==1:
        print("Dzielniki 1 to: 1")
    else:
        print("Dzielniki ",x," to: ",sep='',end='')
        i=1
        while i*i<x:
            if x%i==0:
                print(i,x//i,end=' ')
            i+=1
        if i*i==x:
            print(i)
        else:
            print()
for i in range(5):
    num=int(input())
    podzielniki(num)
    
            
