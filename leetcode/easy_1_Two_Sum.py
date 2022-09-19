# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from ast import List

class Solution:
    def twoSum0(self, nums: List[int], target: int) -> List[int]:
        """ dummy solution, complex n^2"""
        for idx1 in range(len(nums)):
            for idx2 in range(idx1 + 1, len(nums)):
                if(nums[idx1] + nums[idx2] == target):
                    return[idx1, idx2]
    
    def twoSum(nums, target):
        """ better solution using dict """
        seen = dict()
        for idx, number in enumerate(nums):
            value = target - number
            if target - value in seen:
                return [idx, seen[target - value]]

            seen[value] = idx

    tab = [2,7,11,15]
    print(twoSum(tab, 9))