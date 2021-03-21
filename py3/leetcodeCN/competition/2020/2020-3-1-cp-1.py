class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt = [0] * 101
        for item in nums:
            cnt[item] += 1
        print(cnt)
        ans = []
        for item in nums:
            if item:
                ans.append(sum(cnt[:item]))
            else:
                ans.append(0)

        return ans


if __name__ == '__main__':
    obj = Solution()
    ls = [8,1,2,2,3]
    print(obj.smallerNumbersThanCurrent(ls))
