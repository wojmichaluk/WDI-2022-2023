#przeniesienie n krążków z a na c z wykorzystaniem b
def hanoi(n,a,b,c):
    if n>0:
        hanoi(n-1,a,c,b)
        print(a,'->',c)
        hanoi(n-1,b,a,c)

#z wykorzystaniem stosu
def hanoi_stos(n,a,b,c):
    st=[]
    st2=[]
    st.append((n,a,b,c))
    while True:
        if len(st)==0:
            return
        cur=st.pop()
        if cur[0]>0:
            st.append((cur[0]-1,cur[2],cur[1],cur[3]))
            st.append((cur[0]-1,cur[1],cur[3],cur[2]))
            st2.append((cur[1],cur[3]))
        else:
            if len(st2)!=0:
                d=st2.pop()
                print(d[0],'->',d[1])

n=3                      
hanoi(n,1,2,3)
print()
hanoi_stos(n,1,2,3)
print()
#iteracyjnie-pętla
slupki=[]
slupki.append([n-i for i in range(n)])
slupki.append([])
slupki.append([])
last=0
i=0
#print(*slupki)
while True:
    if n%2==0:
        i=(i+1)%3   
    else:
        i=(i+2)%3
    slupki[last].pop()
    slupki[i].append(1)
    print(last+1,'->',i+1)
    last=i
    c,d=(i+2)%3,(i+1)%3
    if slupki[0]==[] and slupki[1]==[]:
        break
    if slupki[c]==[]:
        a=slupki[d].pop()
        slupki[c].append(a)
        print(d+1,'->',c+1)
    elif slupki[d]==[]:
        a=slupki[c].pop()
        slupki[d].append(a)
        print(c+1,'->',d+1)
    else:
        if slupki[c][-1]<slupki[d][-1]:
            a=slupki[c].pop()
            slupki[d].append(a)
            print(c+1,'->',d+1)
        else:
            a=slupki[d].pop()
            slupki[c].append(a)
            print(d+1,'->',c+1)
#print(*slupki)
