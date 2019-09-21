class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0

        while n:
            ans += n % 2
            n = n // 2

        return ans