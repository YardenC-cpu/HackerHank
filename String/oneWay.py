

def oneWay(a, b):
    #create a variable for the count 
    count = 0

    #calculate the len of a and b 
    len_a = len(a)
    len_b = len(b)

    
    # demonstate the 3 cases 

    #1. the string are equal, we are looking for a replacement 
    if len_a == len_b:
        bool = False
        bool = checkCase(a,b)
        if bool == True:
            return True 
    
    # 2. a is bigger than b, we are looking for a deletion 
    if len_b + 1 == len_a:
        bool = False
        bool = checkCase(b, a)
        if bool == True:
            return True
    
    # 2. a is smaller than b, we are looking for a insertion 
    if len_b -1 == len_a:
        bool = False
        bool = checkCase(a, b)
        if bool == True:
            return True

    return False 

#the helper function
def checkCase(short, long):        
    short = list(short)
    long = list(long)

    j = 0
    for i in range(len(short)): 
        item = short[i]
        if item in long:
            long.remove(item)

    if len(long) != 1:
        return False 

    return True

        
a = 'bake'
b = 'bke'
print(oneWay(a,b))