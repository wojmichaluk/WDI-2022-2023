from random import randint

def aryth_dif(T):
    r=T[1]-T[0]
    current_p=current_m=2
    last=T[1]
    longest_p=longest_m=0
    for i in range(2,len(T)):
        if T[i]-last!=r:
            if r<0:
                longest_m=max(longest_m,current_m)
                current_m=2
            elif r>0:
                longest_p=max(longest_p,current_p)
                current_p=2
            r=T[i]-last
        else:
            if r<0:
                current_m+=1
            elif r>0:
                current_p+=1
        last=T[i]
    longest_m=max(longest_m,current_m)
    longest_p=max(longest_p,current_p)
    if longest_m==2:
        longest_m=0
    if longest_p==2:
        longest_p=0
    return longest_p-longest_m

#sztywny przypadek dla N=20
#N=int(input())
N=20
T=[randint(1,99) for _ in range(N)]
for i in range(N):
    if T[i]%2==0:
        if i%2==0:
            T[i]+=1
        else:
            T[i]-=1
print(aryth_dif(T))
