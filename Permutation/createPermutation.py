'''
This problem is taken from LeetCode
Source: https://leetcode.com/problems/permutations/

Defination:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Explanation:
Intuitively, what we want to do here is each step to choose one letter from the array and permutate it to all possible locations. 
We can start by drawing a tree with the string as the root, we will notice that each time we pick a letter and we are left with the rest of the string. 
We then pick at each time where to locate letters from the letter that we left with. 
For example, string [a, b, c] -> [a, b] + [c], [a, c]+[b] for a. 
Many of the questions that often include a tree and a repeating action are involve recursion, so to implement this I will use recursion. 

Our array will be nums, in each stage I will pick a current letter which will be stored in a path variable. At each call of the recursion, 
I will choose another letter from the remaining letters (nums) and add that to the path. When I no longer have a letter left, 
I can append the permutation to my final array, at the end it will store all possible permutations. 

'''

def createPermutation(nums):

    def permuRecursion(nums, path, res):
        if len(nums) == 0:
            res.append(path)

        for i in range(len(nums)):
            permuRecursion(nums[:i]+nums[i+1:], path+[nums[i]], res)

    res = []
    for i in range(len(nums)):
        permuRecursion(nums[i+1:], nums[i], res)


    return res 