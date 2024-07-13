class Solution(object):
    def findDuplicates(self, nums):
        \\\
        :type nums: List[int]
        :rtype: List[int]
        \\\
        dit = {}
        for i in nums:
            if i in dit:
                dit[i] += 1
            else:
                dit[i] = 1
        lst = []
        for key, val in dit.items():
            if val > 1:
                lst.append(key)
        return lst