class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                c = -nums[a]-nums[b]
                if c in nums[b+1:]:
                    tmp = [nums[a], nums[b], c]
                    tmp.sort()
                    ans.append(tmp)

        return list(set(ans))