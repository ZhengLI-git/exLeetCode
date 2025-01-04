#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
# @lc code=end


#set and sort
# def removeDuplicates(self, nums: List[int]) -> int:
# 		nums[:] = sorted(set(nums))
# 		return len(nums)
