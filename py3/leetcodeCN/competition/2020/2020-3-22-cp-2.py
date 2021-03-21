class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        def decompose(data):
            m = int(math.sqrt(data)+2)
            ret = set()
            for i in range(1, m+1):
                if i >= data:
                    break
                if data % i == 0:
                    ret.add(i)
                    ret.add(data//i)
            return list(ret)

        ans = 0
        for item in nums:
            decom = decompose(item)
            if len(decom) == 4:
                ans += sum(decom)

        return ans
