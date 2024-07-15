class Solution(object):
    def isPalindrome(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        st = \\
        for i in s:
            if i.isalpha() or i.isdigit():
                st += i.lower()
        if st == st[::-1]:
            return True
        return False
        