# Given an integer array nums sorted in non-decreasing order, remove
# the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.

# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by
# modifying the input array in-place with O(1) extra memory.

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

def remove_duplicates(nums) -> int:
    list_len = -len(nums)
    i = -2
    k = len(nums)
    while i != list_len:
        if nums[i+1] == nums[i]:
            nums[i+1] = nums[i + 2]
            nums[i + 2] = '_'
            k = k - 1
        i = i - 1
    return k, nums

if __name__ == '__main__':
    nums = [1,1,2]
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    print(remove_duplicates(nums2))
