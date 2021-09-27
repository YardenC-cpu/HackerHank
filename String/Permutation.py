
from collections import defaultdict

def permu(b, s):    
    b = sorted(b)
    s = sorted(s)
    a = 'a'

    if len(s) != len(b):
        return False
    else:
        return b == s

def permuCount(s, b):

    if len(s) != len(b):
        return False 

    #create the dic 
    chars = defaultdict(int)

    #mapping the char to its corresponded times 
    for char_s in s:
        chars[char_s] += 1

    for char_b in b:
        chars[char_b] -= 1
        if chars[char_b] != 0:
            return False 
    
    return True

s = 'yardeno'
b ='arneyd'

#print(permu(s,b))
print(permuCount(s,b))

