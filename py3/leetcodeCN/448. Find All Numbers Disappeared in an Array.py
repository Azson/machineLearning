class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            while nums[i] != i+1:
                #不使用pos存储会出现问题，nums[i]的值被提前替换了？
                pos = nums[i] - 1
                if nums[pos] == nums[i]:
                    break
                nums[i], nums[pos] = nums[pos], nums[i]
                print( nums[i], nums[pos])
        ans =[]
        for i in range(len(nums)):
            if i+1 != nums[i]:
                ans.append(nums[i])

        return ans