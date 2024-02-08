x=a=int(input())
rew=0
while a>0:
    rew=10*rew+a%10 #dla podstawy n - wstawiamy n zamiast 10
    a//=10 #analogicznie
print(x==rew)
