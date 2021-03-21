class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """

        ans = 1 if len(arr) else 0
        pos = {}
        for num in arr:

            if num - difference in pos:
                pos[num] = pos[num - difference] + 1
                ans = max(ans, pos[num])

            else:
                pos[num] = 1

        return ans