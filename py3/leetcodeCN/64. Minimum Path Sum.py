#!/usr/bin/python
# -*- coding: utf-8 -*-
def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[0][0] = grid[0][0]
            elif i == 0:
                dp[0][j] = dp[0][j-1] + grid[0][j]
            elif j == 0:
                dp[i][0] = dp[i-1][0] + grid[i][0]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]

if __name__ == '__main__':
    pass