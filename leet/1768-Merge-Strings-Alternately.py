class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        i, j = 0, 0
        len1, len2 = len(word1), len(word2)
        while i < len1 and j < len2:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1
        while i < len1:
            merged.append(word1[i])
            i += 1
        while j < len2:
            merged.append(word2[j])
            j += 1
        return ''.join(merged)
