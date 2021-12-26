'''
This is NOT a HackerHank problem but rather a problem that apppeared in one of the technical interview I was doing. 
Description: 
We are given two strings and we want to return True if both are permutation of one another (if they are the same). 

-Permutation defination: different ways on which a value canbe rearranged.

Explanation: 
There are two functions here:
1. Permu:
    *Sort each string 
    *Then check if they are equsl 
2.PermuCount:
    *We are using dictionery to count the number of apperances for each letter (on one of the strings) using Counter 
    *We are iterating over the other strinf and each letter we are decreasing its counting in the dictionery 
    *If at the end we are left with any value in the dict that is bigger then 1, we return False 
'''
from collections import Counter

def permu(b, s):    
    b = sorted(b)
    s = sorted(s)

    if len(s) != len(b):
        return False
    else:
        return b == s

def permuCount(s, b):

    if len(s) != len(b):
        return False 

    #create the Counter dict 
    chars = Counter(s)

    #decrement the value of the each letter 
    for char_b in b:
        chars[char_b] -= 1
    
    #if any value in the dict is greater than 1, we returning false 
    for val in chars.values():
        if val > 0:
            return False 
    
    return True

s = 'yarden'
b ='arneyd'

print(permu(s,b))
print(permuCount(s,b))

