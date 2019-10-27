class Solution(object):
    def circularPermutation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: List[int]
        """

        ln = 1 << n
        ans = [0] * (ln)

        for i in range(n):
            st = 1 << i
            step = 1 << (i + 1)
            delta = st
            while True:
                for sz in range(step):
                    if st + sz >= ln:
                        break

                    ans[st + sz] += delta
                st += step * 2
                if st >= ln:
                    break

        for idx, item in enumerate(ans):
            if item == start:
                ans = ans[idx:] + ans[:idx]
        return ans