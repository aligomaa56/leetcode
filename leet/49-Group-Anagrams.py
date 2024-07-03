class Solution(object):
    def groupAnagrams(self, strs):
        \\\
        :type strs: List[str]
        :rtype: List[List[str]]
        \\\
        dit = {}
        for i in strs:
            si = ''.join(sorted(i))
            print(si)
            if si not in dit:
                dit[si] = []
            dit[si].append(i)
        return list(dit.values())
