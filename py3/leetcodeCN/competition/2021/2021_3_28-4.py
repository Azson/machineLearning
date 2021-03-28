class Solution(object):
    def maxNiceDivisors(self, primeFactors):
        """
        :type primeFactors: int
        :rtype: int
        """
        mod = int(1e9+7)
        def qsm(a, b):
            ret = 1
            while (b > 0):
                if (b & 1):
                    ret = (ret * a) % mod
                a = (a * a) %mod
                b >>= 1
            return ret
        fac = primeFactors // 3
        ans = 1
        if (primeFactors % 3 == 1 and primeFactors > 3):
            fac -= 1
            ans = 4
            
        ans *= qsm(3, fac) % mod
        if (primeFactors % 3 == 2):
            ans = ans * 2 % mod
        return ans % mod