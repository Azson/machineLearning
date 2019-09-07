#!/usr/bin/python
# -*- coding: utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        n = len(height)
        l = 0
        r = n-1


        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans



if __name__ == '__main__':
    pass