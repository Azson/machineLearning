class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = 0

        for val in nums:
            two |= one & val
            one ^= val

            three = one&two
            one &= ~three
            two &= ~three
        return one