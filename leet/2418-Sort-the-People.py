class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        combined = list(zip(names, heights))
        
        sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)
        
        sorted_names = [name for name, height in sorted_combined]
        
        return sorted_names
