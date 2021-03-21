class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        for idx in range(n):
            ans.insert(index[idx], nums[idx])

        return ans