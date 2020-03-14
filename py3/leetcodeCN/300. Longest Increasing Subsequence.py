class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        ret = [nums[0]]
        nums.pop(0)
        import bisect

        for item in nums:
            idx = bisect.bisect_left(ret, item)
            # print(idx, ret)
            if idx == len(ret):
                ret.append(item)
            else:
                ret[idx] = item

        return len(ret)


if __name__ == '__main__':
    ls = [10,9,2,5,3,7,101,18]
    obj = Solution()
    print(obj.lengthOfLIS(ls))