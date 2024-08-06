class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        words = s.split()
        
        truncated_words = words[:k]
        
        truncated_sentence = ' '.join(truncated_words)
        
        return truncated_sentence
