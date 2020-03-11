class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        val = sum(A)
        if val % 3:
            return False
        val //= 3

        sm = 0
        c = 0
        for item in A:
            sm += item
            if sm == val:
                sm = 0
                c += 1
        if val == 0:
            return c >= 3
        return c == 3