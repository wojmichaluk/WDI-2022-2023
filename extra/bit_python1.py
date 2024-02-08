if __name__=='__main__':
"""
#1

    string="Hello world"
    for letter in string:
        print(letter,end=' ')
    a=None
"""
"""
komentarz
wielolinijkowy
"""
"""
#2
print()
name=input()
age=int(input())
print(name,end=' ')
if age<18:
    print("nie",end=' ')
print("jest pełnoletni i ma",age, "lat.")
#3
num1=int(input())
num2=int(input())
print(num1+num2)

#4.1
for i in range(1,21):
    print(i,end='\t')

#4.2
for i in range(21):
    if i%3==0:
        print(i,end='\t')

print()
for i in range(21):
    if i%3==0 and i%2!=0:
        print(i,end='\t')

#5
print()
for i in range(1,101):
    print(i,end=' ')
    if i%3==0:
        print("Fizz",end='')
    if i%5==0:
        print("Buzz",end='')
    print()

#6
suma=0
while (temp:=int(input()))!=0:
    suma+=temp
print(suma)

#7
for i in range(1,101):
    if i%2==0 and i%3==0 or (i%5==0 or i%7==0):
        print(i)

#8
num=int(input())
suma_cyfr=0
ilosc_cyfr=0
temp=num
if temp==0:
    ilosc_cyfr=1
else:
    while temp>0:
        suma_cyfr+=temp%10
        temp//=10
        ilosc_cyfr+=1
print(suma_cyfr,ilosc_cyfr)

#9
string=input()
print(len(string),string[::-1])

#10
rows=int(input())
for i in range(rows):
    print((2*i+1)*'x')
"""
    
