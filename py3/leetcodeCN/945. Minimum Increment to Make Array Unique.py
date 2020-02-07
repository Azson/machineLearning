class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        mx = 40000*2+10
        position = [0] * mx
        sz = len(A)
        for item in A:
            position[item] += 1

        for val in range(0, mx):
            if(position[val] > 1):
                tmp = position[val] - 1
                position[val+1] += tmp
                ans += tmp
            if position[val]:
                sz -= position[val]
                if not sz:
                    break
        return ans