class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """

        def cmp(x, y):
            if x[1] == y[1]:
                return -1 if x[0] > y[0] else 1
            return -1 if x[1] > y[1] else 1

        from functools import cmp_to_key
        import heapq

        ret = []
        for i in range(n):
            ret.append([speed[i], efficiency[i]])

        mod = 10**9 + 7
        ret = sorted(ret, key=cmp_to_key(cmp))
        sm = 0
        ans = 0
        pqe = []
        for i in range(n):
            sm += ret[i][0]
            heapq.heappush(pqe, ret[i][0])
            if len(pqe) > k:
                top = heapq.heappop(pqe)
                sm -= top
            ans = max(ans, sm*ret[i][1])

        return ans % mod