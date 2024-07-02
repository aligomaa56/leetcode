class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 1
        for i in nums:
            total *= i
        if total > 0:
            return 1
        if total < 0:
            return -1
        if total == 0:
            return 0