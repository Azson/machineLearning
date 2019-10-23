class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """

        ans = 0
        ban = 0
        for i in s:
            if i == 'R':
                ban -= 1
            else:
                ban += 1
            if not ban:
                ans += 1

        return ans