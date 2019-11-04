class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
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

        return  ans
        '''
        res, head = [0], 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res
        '''