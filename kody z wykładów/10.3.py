def onp(s):
    tmp_stack=[]
    new_s=''
    while s!='':
        

def obl_wart(s):
    ops=['+','-','*','/','**']
    elems=s.split(' ')
    stack=[]
    while elems!=[]: 
        if elems[0] in ops:
            val=ev(stack[-2],stack[-1],elems[0])
            stack=stack[:len(stack)-2]+[val]
        else:
            stack+=[elems[0]]
        elems=elems[1:]
    return stack[0]

def ev(m,n,op):
    m,n=float(m),float(n)
    if op=='+':
        return m+n
    elif op=='-':
        return m-n
    elif op=='*':
        return m*n
    elif op=='/':
        return m/n
    elif op=='**':
        return m**n

napis="21 7 / 4 - -15 *"
print(obl_wart(napis))
