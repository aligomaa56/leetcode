class Solution(object):
    def topKFrequent(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
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
            lst.append((val, key))
        lst.sort(reverse=True)
        result = []
        for key, val in lst[:k]:
            result.append(val)
        return result