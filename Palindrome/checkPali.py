'''
Valid Palindone- this problem is taken from LeetCode 
Source: https://leetcode.com/problems/valid-palindrome/

Defination: 
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.


Explanation:
    *we are organizing the string as a list, removing any non-alphabetic chars and convert into lower case 
    *we are counting the number of occurances for each letter 
    *we are checking for each occurances if it even or odd 
    *if odd
        -we need to make sure that also the length is an odd number 
        -since any palindome can have only one character that will stand alone, we want to make sure that we only have this case one time 

'''
from collections import Counter

def checkPali(s):

    s = s.lower()
    s = list("".join(l for l in s if l.isalpha()))

    print(s)
    s_dict = Counter(s)
    booleanPali = False 

    for i in s_dict:
        #when we have an odd count 
        if s_dict[i] % 2 == 1:
            if len(s) % 2 == 0:
                return False
            else:
                if booleanPali:
                    return False 
                booleanPali = True 

    return True 

print(checkPali("race a car"))