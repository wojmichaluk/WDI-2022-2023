x=0.5**0.5
y=x
for i in range(100):
    x=(0.5+0.5*x)**0.5
    y*=x
print('Wartosc pi wynosi około',2*(1/y))
