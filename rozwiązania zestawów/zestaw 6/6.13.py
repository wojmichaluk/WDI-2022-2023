def splits(num, j, split):
    if num==0 and split[1]!=0:
        for k in range(len(split)-1,0,-1):
            if split[k]!=0:
                break
        for i in range(k):
            print(split[i],'+',sep='',end='')
        print(split[k])
        return
    if j==0:
        mini=1
    else:
        mini=split[j-1]
    for i in range(mini,num+1):
        split[j]=i
        splits(num-i,j+1,split)
        split[j]=0

n=int(input())
t=[0 for _ in range(n)]
splits(n,0,t)
