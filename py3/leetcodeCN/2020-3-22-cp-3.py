class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        '''
        0:up, 1:down,
        2:left, 3:right
        '''
        def can_go(s1, s2, dir):
            if s1 == 1:
                if dir == 2:
                    return s2 in [1, 4, 6]
                elif dir == 3:
                    return s2 in [1, 3, 5]
                return False
            if s1 == 2:
                if dir == 0:
                    return s2 in [2, 3, 4]
                elif dir == 1:
                    return s2 in [2, 5, 6]
                return False
            if s1 == 3:
                if dir == 2:
                    return s2 in [1, 4, 6]
                elif dir == 1:
                    return s2 in [2, 5, 6]
                return False
            if s1 == 4:
                if dir == 3:
                    return s2 in [1, 3, 5]
                elif dir == 1:
                    return s2 in [2, 5, 6]
                return False
            if s1 == 5:
                if dir == 2:
                    return s2 in [1, 4, 6]
                elif dir == 0:
                    return s2 in [2, 3, 4]
                return False
            if s1 == 6:
                if dir == 3:
                    return s2 in [1, 3, 5]
                elif dir == 0:
                    return s2 in [2, 3, 4]
                return False

        def ok(y, x):
            if 0 <= y < m and 0 <= x < n:
                return True
            return False

        def bfs():
            queue = [[0,0]]

            while len(queue) > 0:
                y, x = queue.pop(0)

                if y == m-1 and x == n-1:
                    return True
                vis[y][x] = True

                for i in range(4):
                    new_y = y+dy[i]
                    new_x = x+dx[i]
                    if ok(new_y, new_x) and vis[new_y][new_x] == False and \
                            can_go(grid[y][x], grid[new_y][new_x], i):
                        queue.append([new_y, new_x])

            return False
        vis = [[False for i in range(n)] for j in range(m)]

        ans = bfs()
        return ans
