'''
From Intrerview Preparation Kit on HackerHank. 
Source: https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


Description:
Starting with a 1-indexed array of zeros and a list of operations, 
for each operation add a value to each the array element between two given indices, 
inclusive. Once all operations have been performed, return the maximum value in the array.

Explanation:
*We will create a new array filled with 0's of n+1 length (this will give us a space to add the k to a and b) 
*We will find the a, b and k in each subarray (indecies 0, 1, 2)
*We want to find the slope that k is giving us, for that we will increase the number in position a-1 by k  
and will decrease the number in position b by 10
*Then we can calculate the scope by summing the positive element in the array 
'''


def arrayManipulation(n, queries):
    #we are using n+1 because we are keeping b as it is (and not b-1)
    arr = [0] * (n+1)


    for query in queries:
        #subtracting 1 to match the indecies 
        a = query[0] - 1
        b = query[1]
        k = query[2]

        arr[a] += k 
        arr[b] -= k


    current = 0
    max_value = 0 
    for val in arr:
        current += val 
        if current > max_value:
            max_value = current 

    return max_value


queries = [[2,6,8], [3,5,7], [1,8,1], [5,9,15]] 
n = 10
print(arrayManipulation(n, queries))


'''
expected answer:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
1. a = 2, b = 6, k=8
-> [0, 8, 0, 0, 0, 0, -8, 0, 0, 0, 0]
2. a = 3, b = 5, k = 7 
-> [0, 8, 7, 0, 0, -7, -8, 0, 0, 0, 0]
3. a = 1, b = 8, k = 1
-> [1, 8, 7, 0, 0, -7, -8, 0, -1, 0, 0]
4. a = 5, b = 9, k = 15
-> [1, 8, 7, 0, 15, -7, -8, 0, -1, -15, 0]
max_value = 1+8+7+15 =  31
'''


