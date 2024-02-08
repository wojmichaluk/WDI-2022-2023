n=int(input())
for i in range(n):
    for j in range(n):
        if i%2==j%2:
            print('X',end='')
        else:
            print('.',end='')
    print()
