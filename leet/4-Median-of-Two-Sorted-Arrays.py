class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        \\\
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        \\\
        z = sorted(nums1 + nums2)

        if len(z) % 2 == 0:
            return (z[len(z) // 2 -1] + z[len(z) // 2]) / 2.0
        else:
            return z[len(z) // 2]