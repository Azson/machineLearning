#!/usr/bin/python
# -*- coding: utf-8 -*-


def maxSubArray(nums):
    length = len(nums)
    sums = nums[0]
    ans = max(nums)
    l = 0
    for i in range(1, length):
        while l < i and sums < 0:
            sums -= nums[l]
            l += 1
        sums += nums[i]
        ans = max(sums, ans)
    return ans


if __name__ == '__main__':
    while True:
        nums = str(input())[1:-1].split(',')
        nums = list(map(int, nums))
        print(maxSubArray(nums))
    pass