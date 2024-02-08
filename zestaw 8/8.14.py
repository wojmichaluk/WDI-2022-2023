def f(a,b):
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
        print(i,j,f(i,j))
#przy f(4,1)... długo myśli :)
