

def isUnique(s):


    #we want to create an array of 128 false values
    bool_arr = [False for i in range(1, 129)]

    for i in range(len(s)):
        #for each letter we want to check its position in the array
        val = ord(s[i])
        #then, we want to check rather it is true (means that I saw this letter before), if true return false
        if bool_arr[val] == True:
            return False 
        #else, mark the location of the letter as true and move to the next letter 
        bool_arr[val] = True 
    
    return True

s = 'erbbbbbbb'
print(isUnique(s))
