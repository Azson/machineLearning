class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        now = list(range(n))
        now = [list(range(n)), list(range(n))]
        ans = 0
        def ok():
            for i in range(n):
                if (i != now[(ans) % 2][i]):
                    return False
            return True
        
        while (True):
            for i in range(n-1, -1, -1):
                if (i % 2 == 0):
                    now[(ans+1) % 2][i] = now[(ans) % 2][i // 2]
                else:
                    now[(ans+1) % 2][i] = now[(ans) % 2][n//2 + (i-1)//2]
            # print(now[(ans + 1) % 2])
            ans += 1
            if (ok()):
                break
        return ans
