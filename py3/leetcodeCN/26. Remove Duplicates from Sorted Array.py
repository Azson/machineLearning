class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s, h = 0, 1

        for h in range(1, len(nums)):
            if nums[s] != nums[h]:
                s += 1
                nums[s] = nums[h]
        while(s+1 < len(nums)):
            del nums[-1]
        '''
        
        ln = len(nums)

        for idx in range(1, len(nums)):
            # print(idx, ln)
            if nums[idx] == nums[idx - 1]:
                t = 1
                while idx + t < ln:
                    if nums[idx + t] != nums[idx]:
                        break
                    t += 1

                for tt in range(idx + t, ln):
                    nums[tt - t] = nums[tt]
                for i in range(t):
                    del nums[-1]
                    ln -= 1
            #放到if内层和外层break效果不一样！？
            if idx + 1 >= ln:
                break

        return len(nums)
        '''