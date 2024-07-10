class Solution(object):
    def subarraySum(self, nums, k):
        \\\
        :type nums: List[int]
        :type k: int
        :rtype: int
        \\\
        count = 0
        cumulative_sum = 0
        cumulative_sum_frequency = {0: 1}
        for num in nums:
            cumulative_sum += num
            if (cumulative_sum - k) in cumulative_sum_frequency:
                count += cumulative_sum_frequency[cumulative_sum - k]
            if cumulative_sum in cumulative_sum_frequency:
                cumulative_sum_frequency[cumulative_sum] += 1
            else:
                cumulative_sum_frequency[cumulative_sum] = 1
        return count
