class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        score = 0
        lst = []
        for arr in accounts:
            for j in arr:
                score += j
            lst.append(score)
            score = 0
        return max(lst)
