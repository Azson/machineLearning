#!/usr/bin/python
# -*- coding: utf-8 -*-
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = [0 for i in range(len(nums) + 1)]
        for i in range(len(nums)):
            self.nums[i+1] = self.nums[i] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j+1] - self.nums[i]

if __name__ == '__main__':
    pass