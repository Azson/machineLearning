class Solution(object):
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        path = []
        MOD = int(1e9+7)
        for item in nums1:
            path.append((item, 0))
        for item in nums2:
            path.append((item, 1))
        path = sorted(path)
        ln = len(path)
        sm = [0, 0]
        i = 0
        while i < ln:
            if (i+1) < ln and path[i][0] == path[i+1][0]:
                sm = [(max(sm) + path[i][0]) % MOD ] * 2
                i += 2
            else:
                sm[path[i][1]] += path[i][0] % MOD
                i += 1

        return max(sm) % MOD
