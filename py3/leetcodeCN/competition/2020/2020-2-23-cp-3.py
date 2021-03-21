class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        import math

        half = int(math.sqrt(num+2))+2
        ans = None
        tmp = None

        for st in range(1, half):
            if (num+1) % st == 0:
                tmp = (num+1) // st
            if (num+2) % st == 0:
                tmp = (num+2) // st

            if tmp and (not ans or  abs(ans[0] - ans[1]) > abs(st - tmp)):
                ans = [st, tmp]
                tmp = None

        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.closestDivisors(1))