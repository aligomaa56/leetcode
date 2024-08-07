class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        xor_result = 0
        for i in range(n):
            xor_result ^= start + 2 * i
        return xor_result
