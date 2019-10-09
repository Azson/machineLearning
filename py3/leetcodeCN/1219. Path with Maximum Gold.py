class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        ans = 0
        vis = [[0 for j in range(m)] for i in range(n)]

        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]


        def dfs(y, x, gold):

            vis[y][x] = 1
            t = gold
            pre = [0, 0]
            for dir in range(4):
                yy = y+dy[dir]
                xx = x+dx[dir]
                if(is_ok(yy, xx) and grid[yy][xx] and not vis[yy][xx]):
                    tmp = dfs(yy, xx, gold+grid[yy][xx])
                    t = max(t, tmp)

            vis[y][x] = 0

            return t


        def is_ok(y, x):
            if(y >=0 and y < n and x >= 0 and x < m ):
                return True
            return False

        for y in range(n):
            for x in range(m):
                if(grid[y][x]):
                    ans = max(ans, dfs(y, x, grid[y][x]))

        return ans


if __name__ == '__main__':
    obj = Solution()
    grid = [
        [0,6,0],
        [5,8,7],
        [0,9,0]
    ]

    print(obj.getMaximumGold(grid))