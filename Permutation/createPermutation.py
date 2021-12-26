'''
This problem is taken from LeetCode
Source: https://leetcode.com/problems/permutations/

Defination:
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Explanation:
Intuitively, what we want to do here is each step to choose one letter from the array and permutate it to all possible locations. 
We do so by iterating throught the array and each i position we are "removing" it from the array and append it to the path, we stopped when the original array is 
empty and the path is full. We keep track of the pemutation that we got.

We can start this problem by drawing a tree with the string as the root, we will notice that each time we pick a letter we want to "remove" it from the nums and 
append it to the path. 
For example, string [a, b, c] -> [b, c] + [a] -> [c] + [a, b] -> [a,b,c] for index 0 
Since nums become [b,c] we are also the permutaiton on it and we also will have [b, c] + [a] -> [b] + [a, c] -> [a,c,b] for index 1
Many of the questions that often include a tree and a repeating action are involve recursion, so to implement this I will use recursion. 

Our array will be nums, in each stage I will pick a current letter which will be stored in a path variable. At each call of the recursion, 
I will choose another letter from the remaining letters (nums) and add that to the path. When I no longer have a letter left, 
I can append the permutation to my final array, at the end it will store all possible permutations.

The time complexity of this algorithm is O(N!), this is also the number of permutaiton that can be formed. 

'''

def createPermutation(nums, path, res):

    def permuRecusrsive(nums, path, res):
        if len(nums) == 0:
            res.append(path)

        for i in range(len(nums)):
            permuRecusrsive(nums[:i]+nums[i+1:], path+[nums[i]], res)

        return res


    return permuRecusrsive(nums, [], [])

nums = [1,2,3]
print(createPermutation(nums, [], []))