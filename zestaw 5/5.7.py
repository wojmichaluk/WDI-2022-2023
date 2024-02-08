def addition(*args):
    (re1,im1)=args[0]
    (re2,im2)=args[1]
    return (re1+re2,im1+im2)

def sub(*args):
    (re1,im1)=args[0]
    (re2,im2)=args[1]
    return (re1-re2,im1-im2)

def multi(*args):
    (re1,im1)=args[0]
    (re2,im2)=args[1]
    return (re1*re2-im1*im2,re1*im2+re2*im1)

def division(*args):
    (re1,im1)=args[0]
    (re2,im2)=args[1]
    return((re1*re2+im1*im2)/(re2**2+im2**2),(re2*im1-re1*im2)/(re2**2+im2**2))

def power(*args):
    comp=args[0]
    comp=complex(comp[0],comp[1])
    p=args[1]
    res=str(comp**p)
    pos=res.find('+')
    if pos==-1:
        pos=res.rfind('-')
    if pos!=-1:
        return (float(res[1:pos]),float(res[pos:len(res)-2]))
    else:
        pos=res.find('j')
        return(0,float(res[:pos]))

def solve(*args):
    (ra,ia)=args[0]
    (rb,ib)=args[1]
    (rc,ic)=args[2]
    (dr,ir)=sub(power((rb,ib),2),multi((4,0),multi((ra,ia),(rc,ic))))
    (dr_r,ir_r)=power((dr,ir),0.5)
    x1=division(sub(multi((-1,0),(rb,ib)),(dr_r,ir_r)),multi((2,0),(ra,ia)))
    x2=division(addition(multi((-1,0),(rb,ib)),(dr_r,ir_r)),multi((2,0),(ra,ia)))
    return x1,x2

(ra,ia,rb,ib,rc,ic)=input().split(',')
(ra,ia,rb,ib,rc,ic)=int(ra),int(ia),int(rb),int(ib),int(rc),int(ic)
print(solve((ra,ia),(rb,ib),(rc,ic)))
