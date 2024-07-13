def a_and_b():
    n=int(input())
    a_0=0
    a_1=1
    b_0=b_1=2
    if n==a_0:
        print(b_0)
    else:
        return
    n=int(input())
    if n==a_1:
        print(b_1)
    else:
        return
    a_curr=a_1-b_1*a_0
    a_prev=a_1
    a_prev_prev=a_0
    b_prev=b_1
    while True:
        n=int(input())
        if n==a_curr:
            b_curr=b_prev+2*a_prev
            print(b_curr)
            a_prev_prev,a_prev,a_curr=a_prev,a_curr,a_curr-b_curr*a_prev
            b_prev=b_curr
        else:
            break
    return

a_and_b()
