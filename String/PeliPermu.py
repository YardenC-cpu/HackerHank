
from collections import defaultdict

def pelidomePermu(s):
    s = s.replace(" ", "")
    s = s.lower()
    s_list = list(s)
    checkOdd = False  

    #create a dict of the array
    chars = defaultdict(s)

    #mapping the char to its corresponded times 
    for char_s in s_list:
        num = ord(char_s)
        chars[num] += 1

    #check that we have only one appearance of any letter with odd occurances 
    for i in chars:
        if chars[i] %2 ==1: #when we see an odd count 
            if len(s_list) %2 == 0: #if it is an even list, return False immidiatly
                return False 
            else: #if not, we just want to make sure that it is one like this
                if checkOdd:
                    return False
            checkOdd = True 
    return True 

   

a = 'Tado cat'

print(pelidomePermu(a))
    