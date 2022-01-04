'''
This question is taken from a coding interview that I previouly had. 

Description: 
We are given a array that represents two words ['c', 'a','r','t', 'h', 'e'] and an index which represent the end of the first word. 
In this case the index will be 3. 
The restriction was a space complexity of O(1) 

Explanation:
The Brute force will be to pop a letter and insert it in the first positon:
We will pop the letters one by one starting at the index until the end. In each time we will push the pop word in the begining 
carthe-> pop(e) -> append(e)->ecarth->pop(h)->append(h)->hecart->pop(t)->append(t)->thecar
This will result a timpe complexity of O(N^2), since the insert operation has a time complexity of O(N)


'''

def changeWord(arr, firstWord):
    for i in range(len(arr)-1, firstWord-1, -1):
        print(i)
        char_arr = arr.pop()
        print(char_arr)
        arr.insert(0, char_arr) #insert is taking O(N), so again we have O(N^2)
        print(arr)
  
    
    return arr


arr = ['c', 'a','r','t', 'h', 'e']
print(changeWord(arr, 3))