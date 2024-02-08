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
    comp=complex(args[0][0],args[0][1])
    p=complex(args[1][0],args[1][1])
    return comp**p

(re1,im1)=input().split(',')
re1,im1=int(re1),int(im1)
(re2,im2)=input().split(',')
re2,im2=int(re2),int(im2)
print(addition((re1,im1),(re2,im2)))
print(sub((re1,im1),(re2,im2)))
print(multi((re1,im1),(re2,im2)))
print(division((re1,im1),(re2,im2)))
print(power((re1,im1),(re2,im2)))
