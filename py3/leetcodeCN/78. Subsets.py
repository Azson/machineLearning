class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        for i in range(1 << len(nums)):
            tmp = []
            c = 0
            while i:
                #考虑使用更pythonic的方法，列表expression
                if i % 2:
                    tmp.append(nums[c])
                c += 1
                i = i // 2
            ans.append(tmp)
        return ans