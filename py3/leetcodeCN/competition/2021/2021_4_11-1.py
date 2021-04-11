class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 1
        for num in nums:
            if num == 0:
                return 0
            ret *= num
        return 1 if ret > 0 else -1