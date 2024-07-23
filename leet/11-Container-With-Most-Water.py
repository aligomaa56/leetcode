class Solution(object):
    def maxArea(self, height):
        \\\
        :type height: List[int]
        :rtype: int
        \\\
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            if height[left] < height[right]:
                current_area = height[left] * width
                left += 1
            else:
                current_area = height[right] * width
                right -= 1
            max_area = max(max_area, current_area)
        return max_area