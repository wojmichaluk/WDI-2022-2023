def rewers(n):
    rew=0
    while n>0:
        rew=10*rew+n%10 
        n//=10 
    return rew

for n in range (197,200):
    print()
    while n!=rewers(n):
        print(n)
        n+=rewers(n)
    print('koniec')
