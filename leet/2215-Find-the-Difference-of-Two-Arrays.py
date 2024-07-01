class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        lst1, lst2 = set(nums1), set(nums2)
        answer = [list(lst1 - lst2), list(lst2 - lst1)]
        return answer