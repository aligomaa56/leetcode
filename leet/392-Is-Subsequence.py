class Solution(object):
    def isSubsequence(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: bool
        \\\
        if s == t:
            return True
        i = 0
        for j in range(len(t)):
            if i < len(s) and s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
        return False
