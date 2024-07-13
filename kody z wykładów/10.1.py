from functools import cache

#rekurencyjnie
@cache
def f(a,b):
    if a==0:
        return b+1
    if b==0:
        return f(a-1,1)
    return f(a-1,f(a,b-1))

#iteracyjnie
"""def f_iter(a,b):
    stack=[(a,b)]
    res=0
    flag=True
    while len(stack)>1 or res==0:
        tup=stack[-1]
        if tup[0]==0:
            res+=tup[1]+1
            stack=stack[:len(stack)-1]
            flag=False
        if len(stack)==0:
            break
        tup=stack[-1]
        if tup[1]==0:
            stack=stack[:len(stack)-1]+[(tup[0]-1,1)]
            flag=False
        if flag:
            stack=stack[:len(stack)-1]+[(a,b-1)]
        flag=True
    return res"""
def f_iter(a,b):
    st=[]
    st.append(a)
    st.append(b)
    while True:
        b=st.pop()
        if len(st)==0:
            return b
        a=st.pop()
        if a==0:
            st.append(b+1)
        elif b==0:
            st.append(a-1)
            st.append(1)
        else:
            st.append(a-1)
            st.append(a)
            st.append(b-1)

for i in range(6):
    for j in range(6):
        print(i,j,f_iter(i,j))
        print(i,j,f(i,j))
#liczy do f(4,0)
