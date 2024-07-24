class Solution(object):
    def removeDuplicates(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        write_index = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                write_index += 1
                nums[write_index] = nums[i]
        return write_index + 1
