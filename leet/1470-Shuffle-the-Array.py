class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        x, y = nums[:n], nums[n:]
        ans = []
        for i in range(len(x)):
            ans.append(x[i])
            ans.append(y[i])
        return ans