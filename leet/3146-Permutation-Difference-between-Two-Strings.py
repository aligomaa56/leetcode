class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        score = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    score += abs(i - j)
        return score