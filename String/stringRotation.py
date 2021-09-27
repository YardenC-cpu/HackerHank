def checkRotation(a,b):

    a = list(a)
    b = list(b)
    x =[]
    y = []

    if len(a) != len(b):
        return False

    for i in range(len(a)):
        if a[i] == b[0]:
            x = a[0:i]
            y = a[i:len(a)]
            break


    if y+x == b:
        return True

    return False   


a = "watermelon"
b = "termelonha"
print(checkRotation(a,b))



#in this case we have a method IsSubstring to check. 
# if we have two strings s1,s2 
#and we know that there is a rotation point, so if we break s1 into two parts - x,y 
# s1 is basically xy, and respectfully s2 is yx 
#now, since we are looking for the substring we can assume that xyxy will include yx 
#hecne, we can use the fuction isSubstring(s1s1, s2)

