class Solution(object):
    def domino(self, n, m, broken):
        """
        :type n: int
        :type m: int
        :type broken: List[List[int]]
        :rtype: int
        """
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        match = [-1] * n * m

        #存储匹配的时候用id比较方便，寻找邻点使用坐标系方便
        pos2id = lambda y, x:y * m + x
        id2pos = lambda id:[id // m, id % m]

        #匈牙利求解最大匹配数
        def edmon_match(now_id):
            pos = id2pos(now_id)
            if vis[now_id]:
                return 0
            vis[now_id] = 1

            for i in range(4):
                new = [pos[0] + dy[i], pos[1] + dx[i]]

                if (ok(*new)):
                    new_id = pos2id(*new)
                    if (match[new_id] == -1 or edmon_match(match[new_id])):
                        match[now_id] = new_id
                        match[new_id] = now_id
                        return 1

            return 0

        def ok(y, x):
            if y >= 0 and y < n and x >= 0 and x < m and G[pos2id(y, x)]:
                return True
            return False

        ans = 0
        G = [1] * n * m

        for item in broken:
            G[pos2id(item[0], item[1])] = 0

        for id in range(n * m):
            now = id2pos(id)

            if (ok(*now) and match[id] == -1):
                vis = [0] * n * m
                ans += edmon_match(pos2id(now[0], now[1]))

        return ans


if __name__ == '__main__':
    n = 3
    m = 3
    broken = [[1,1]]#[[1, 0], [1, 1]]

    obj = Solution()

    print(obj.domino(n, m, broken))