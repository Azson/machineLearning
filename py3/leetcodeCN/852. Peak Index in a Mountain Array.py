class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = [0, 0]
        for idx, val in enumerate(A):
            if ans[0] < val:
                ans[1] = idx
                ans[0] = val
        return ans[1]