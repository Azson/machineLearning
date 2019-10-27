class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        mp = {}
        for item in arr:
            if item in mp:
                mp[item] += 1
            else:
                mp[item] = 1

        return len(set(mp.values())) == len(mp.values())