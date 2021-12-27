'''
2Sum, taken from LeetCode. See the harder version of it in the 3sum question) 
Source: https://leetcode.com/problems/two-sum/

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Explanation:
Brute Force:
    We are going over the array, having two pointers. 
    For each pair, we will decrease nums[i] from the target and will check rather we have the result in the array, we will return the index  

This solution requires O(N^2) since we are checking the calculation for each value in the list, for each element. 
Since we are searching for a specific number each time (target-current), we can store the values in a dictionery and have a constant time of search.
This leaves us with time complexity of O(N) and a space memory of O(N)

'''


def twoSum(nums, target):
    sum_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in sum_dict:
            return sum_dict[complement], i
        sum_dict[nums[i]] = i 

    return 


nums = [2,5,5,11]
target = 10 
print(twoSum(nums, target))
