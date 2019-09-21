class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = []
        for val in range(num+1):
            cnt = 0
            while val:
                cnt += val % 2
                val >>= 1
            ans.append(cnt)
        return ans
        #可以试试dp