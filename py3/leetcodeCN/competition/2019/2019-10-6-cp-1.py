class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        ans = [0] * 2
        for num in chips:
            ans[num % 2] += 1

        return min(ans[1], ans[0])