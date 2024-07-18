class Solution(object):
    def reverseString(self, s):
        \\\
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        \\\
        lft = 0; rit = len(s)-1
        while lft < rit:
            s[lft], s[rit] = s[rit], s[lft]
            lft += 1
            rit -= 1
