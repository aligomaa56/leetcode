class Solution(object):
    def longestCommonPrefix(self, strs):
        \\\
        :type strs: List[str]
        :rtype: str
        \\\
        if not strs:
            return \\
        
        s = min(strs, key=len)
        
        for i in range(len(s)):
            for word in strs:
                if word[i] != s[i]:
                    return s[:i]
        return s
