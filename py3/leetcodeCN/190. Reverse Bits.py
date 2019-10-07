class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            ret = ret * 2 + n % 2
            n = n // 2
        return ret