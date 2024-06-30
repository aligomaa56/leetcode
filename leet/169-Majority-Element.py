class Solution(object):
    def majorityElement(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        for i in range(len(nums)):
            if nums.count(nums[i]) > len(nums) // 2:
                return(nums[i])