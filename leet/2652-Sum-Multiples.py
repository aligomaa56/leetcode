class Solution(object):
    def sumOfMultiples(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [num for num in range(1,n+1) if num%3==0 or num%5==0 or num%7==0]
        
        return sum(nums)
    