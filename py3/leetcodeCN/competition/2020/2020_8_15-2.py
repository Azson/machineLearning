class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

#
# 牛牛经过的房间数。
# @param n int整型 
# @param x int整型 
# @param Edge Point类一维数组 
# @return int整型
#
class Solution:
    def solve(self , n , x , Edge ):
        # write code here

        def dfs(node, dist):
            qe = [node]
            dist[node] = 0
            while len(qe) > 0:
                u = qe.pop(0)
                for v in tree[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        qe.append(v)

        tree = dict()
        for p in Edge:
            if p.x in tree:
                tree[p.x].append(p.y)
            else:
                tree[p.x] = [p.y]
            if p.y in tree:
                tree[p.y].append(p.x)
            else:
                tree[p.y] = [p.x]
        d1 = [-1] * (n+1)
        dx = [-1] * (n+1)

        dfs(1, d1)
        dfs(x, dx)
        print(d1, dx)
        ans = 0
        for v in range(1, n+1):
            if d1[v] > dx[v]:
                ans = max(ans, d1[v]+1)

        return ans


if __name__ == "__main__":
    s = Solution()
    n, x = 9, 7
    edge = [Point(1,2), Point(2,3), Point(3,4), Point(2,5), Point(1,6), Point(5, 7), Point(5, 8), Point(8, 9)]
    print(s.solve(n, x, edge))