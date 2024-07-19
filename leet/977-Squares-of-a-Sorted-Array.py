class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr = [0] * n
        p = n - 1
        l, r = 0, n - 1
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                arr[p] = nums[l] ** 2
                l += 1
            else:
                arr[p] = nums[r] ** 2
                r -= 1
            p -= 1
        return arr