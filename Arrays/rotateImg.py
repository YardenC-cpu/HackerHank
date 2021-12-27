'''
Rotate Image, taken from LeetCode 
Source: https://leetcode.com/problems/rotate-image/

Description:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Explanation:
I have used an extra space (deep copy) to keep track of the location of each variable. Then it is just figuring out that each value is mapped to its
new position. 
From the end of the array- each variable in the last array is mapped to the first element in each subarray and so forth. 
In general, if this problem include only a linear array we can perform this algorithm in O(N) time using a dictionery to keep track of the location 

Time complexity of O(N^2) and memory of O(N)

'''

import copy

def rotate(matrix):
    matrix_temp = copy.deepcopy(matrix) 
        
    k = 0
    for i in range(len(matrix)-1, -1, -1):
        h = 0
        for j in range(len(matrix)): #starts from 0 
            matrix[j][k] = matrix_temp[i][h] 
            h += 1
        k += 1 


