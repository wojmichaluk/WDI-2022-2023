def wyraz(s1,s2,n,curr='',i=0):
    if waga(s1,curr):
        return True, curr
    if i<n:
        return wyraz(s1,s2,n,curr+s2[i],i+1) or wyraz(s1,s2,n,curr,i+1)
    return False

def waga(s1,s2):
    samogloski=set(['a','e','i','o','u','y'])
    is1=is2=waga1=waga2=0
    for char in s1:
        if char in samogloski:
            is1+=1
        waga1+=ord(char)
    for char in s2:
        if char in samogloski:
            is2+=1
        waga2+=ord(char)
    return waga1==waga2 and is1==is2

str1=input()
str2=input()
print(wyraz(str1,str2,len(str2)))
