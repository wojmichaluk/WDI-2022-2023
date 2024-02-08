def not_cross(x1,x2,y1,y2,our_squares):
    if our_squares==[]:
        return True
    for square in our_squares:
        (xs,xs2,ys,ys2)=square
        if (xs<x1<xs2 and xs2<x2 and (ys<y1<ys2 or ys<y2<ys2)) or ((xs<x1<xs2 or xs<x2<xs2) and ys<y1<ys2 and ys2<y2):
            return False
    return True

def sarea(x1,x2,y1,y2):
    return (x2-x1)*(y2-y1)

def squares(T,index=0,area=0,to_find=13,already_chosen=[]):
    if to_find==0:
        if area==2012:
            return True
        return False
    if index==len(T) or area>2012:
        return False
    x1,x2,y1,y2=T[index]
    if not_cross(x1,x2,y1,y2,already_chosen):
        square_area=sarea(x1,x2,y1,y2)
        already_chosen+=[(x1,x2,y1,y2)]
        if squares(T,index+1,area+square_area,to_find-1,already_chosen):
            return True
    if squares(T,index+1,area,to_find,already_chosen):
        return True
    return False

tab1=[(0,44,0,44),(45,48,45,48),(49,52,49,52),(34,47,21,34)]
tab2=[(57,60,57,60),(61,64,61,64),(65,68,65,68),(1,2,1,2)]
tab3=[(73,76,73,76),(77,78,77,78),(79,80,79,80),(123,144,0,21)]
tab4=[(83,84,83,84),(81,82,81,82),(53,56,53,56),(69,72,69,72)]
T=tab1+tab2+tab3+tab4
print(squares(T))
