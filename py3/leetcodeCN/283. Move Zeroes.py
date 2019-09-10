class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        ls = []
        zero_nums = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                ls.append(i)
                zero_nums += 1
            elif len(ls) > 0:
                nums[ls[0]] = nums[i]
                del ls[0]
                ls.append(i)
        for i in range(zero_nums):
            nums[-i-1] = 0
        #double point need
        '''
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
        '''