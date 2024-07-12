class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        lst = []
        for i in words:
            if separator in i[0] and separator in i[-1]:
                val = i[1:-1].split(separator)
                lst.extend(val)
            else:
                val = i.split(separator)
                lst.extend(val)
        lst = [s for s in lst if s != ""]
        return lst
