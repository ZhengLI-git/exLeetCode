#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i in range(len(nums)):
            if target - nums[i] in index:# check in the key of the dictionary
                return [index[target - nums[i]], i]
            index[nums[i]] = i
        return []     
# @lc code=end

