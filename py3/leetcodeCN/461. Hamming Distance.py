class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while x > 0 and y > 0:
            ans += 1 if x % 2 != y%2 else 0
            x /= 2
            y /= 2
        x = max(x, y)
        while x > 0:
            ans += x%2
            x /= 2
        return ans