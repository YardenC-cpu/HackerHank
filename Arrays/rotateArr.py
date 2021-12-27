'''
Rotate Array, taken from LeetCode 
Source: https://leetcode.com/problems/rotate-array/

Description:
Given an array, rotate the array to the right by k steps, where k is non-negative.

Explanation:
The kind of questions that when you draw it, you see the solution. 
Nothing fancy here, just pop and insert the elements that we are rotating.

Time complexity of O(k) and memory of O(1)

'''


#Time complexity of O(k) and memory of O(1)
def rotate(self, nums, k): 
    add = []                     
    for i in range(k):
        add= nums.pop()
        nums.insert(0, add)




#Time complexity of O(1) and memory space of O(N)
def rotate_another(nums, k):
    #this way we don't have to worry about the case when k > len(nums)
    k = k % len(nums)


    #nums[:] is equivelent of creating a new array
    #nums[-k:] is for picking the last k elements in the array  
    # nums[:-k] is to pick the element from the begining till k
    nums[:] = nums[-k:] + nums[:-k] 

    return nums

print(rotate_another(nums=[1,2,3,4,5,6,7], k= 3))


