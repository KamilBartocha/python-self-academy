# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from ast import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for idx, number in enumerate(nums):
            value = target - number
            if value in seen:
                return [idx, seen[value]]

            seen[value] = idx
