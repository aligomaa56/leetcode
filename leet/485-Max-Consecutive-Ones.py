class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        max_count = 0
        current = 0
        
        for num in nums:
            if num == 1:
                current += 1
            else:
                max_count = max(max_count, current)
                current = 0
    
        max_count = max(max_count, current)
        return max_count
