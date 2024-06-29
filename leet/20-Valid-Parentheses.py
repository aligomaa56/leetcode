class Solution(object):
    def isValid(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        lst = []
        map_ = {')': '(', '}': '{', ']': '['}
        
        for i in s:
            if i in map_.values():
                lst.append(i)
            elif i in map_.keys():
                if not lst or map_[i] != lst.pop():
                    return False
            else:
                return False
        
        return not lst